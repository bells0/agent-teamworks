from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_ROOT = ROOT / "examples" / "commerce-project" / ".agent-teamworks"
RECORD_MARKERS = {
    "role_ids": "team.schema.json",
    "role_id": "role.schema.json",
    "work_item_id": "work-item.schema.json",
    "handoff_id": "handoff.schema.json",
    "decision_id": "decision.schema.json",
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def record_schema_name(record: dict) -> str:
    matches = [schema for key, schema in RECORD_MARKERS.items() if key in record]
    if len(matches) != 1:
        raise AssertionError(f"record must expose exactly one identity key: {record}")
    return matches[0]


class RepositoryValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schemas = {
            path.name: load_json(path) for path in sorted(SCHEMA_DIR.glob("*.schema.json"))
        }
        cls.records = {
            path.relative_to(EXAMPLE_ROOT): load_json(path)
            for path in sorted(EXAMPLE_ROOT.rglob("*.json"))
        }
        cls.team = cls.records[Path("team.json")]
        cls.roles = {
            record["role_id"]: record
            for path, record in cls.records.items()
            if path.parts[0] == "roles"
        }
        cls.work_items = {
            record["work_item_id"]: record
            for path, record in cls.records.items()
            if path.parts[0] == "work-items"
        }
        cls.decisions = {
            record["decision_id"]: record
            for path, record in cls.records.items()
            if path.parts[0] == "decisions"
        }
        cls.handoffs = {
            record["handoff_id"]: record
            for path, record in cls.records.items()
            if path.parts[0] == "handoffs"
        }

    def test_expected_schemas_exist_and_are_valid(self) -> None:
        self.assertEqual(set(self.schemas), set(RECORD_MARKERS.values()))
        for name, schema in self.schemas.items():
            with self.subTest(schema=name):
                Draft202012Validator.check_schema(schema)

    def test_every_example_record_validates(self) -> None:
        checker = FormatChecker()
        for path, record in self.records.items():
            schema_name = record_schema_name(record)
            validator = Draft202012Validator(
                self.schemas[schema_name], format_checker=checker
            )
            errors = sorted(validator.iter_errors(record), key=lambda error: list(error.path))
            with self.subTest(record=str(path)):
                self.assertEqual([], [error.message for error in errors])

    def test_team_roster_has_one_active_binding_per_role(self) -> None:
        self.assertEqual(set(self.team["role_ids"]), set(self.roles))
        self.assertIn(self.team["coordinator_role_id"], self.roles)
        self.assertEqual(
            self.roles[self.team["coordinator_role_id"]]["status"], "active"
        )

        active_refs = [
            role["binding"]["agent_ref"]
            for role in self.roles.values()
            if role["binding"]["state"] == "active"
        ]
        self.assertNotIn(None, active_refs)
        self.assertEqual(len(active_refs), len(set(active_refs)))
        for role in self.roles.values():
            self.assertEqual(role["team_id"], self.team["team_id"])

    def test_work_graph_references_roles_and_has_no_cycles(self) -> None:
        work_ids = set(self.work_items)
        role_ids = set(self.roles)

        for work_id, item in self.work_items.items():
            self.assertEqual(item["team_id"], self.team["team_id"])
            self.assertIn(item["owner_role_id"], role_ids)
            self.assertTrue(set(item["supporting_role_ids"]).issubset(role_ids))
            self.assertTrue(set(item["dependencies"]).issubset(work_ids))
            self.assertNotIn(work_id, item["dependencies"])

            if item["status"] == "done":
                self.assertIn(
                    item["acceptance"]["engineering"], ["passed", "not_required"]
                )
                self.assertIn(
                    item["acceptance"]["user"], ["accepted", "not_required"]
                )

            if item["status"] not in ["backlog", "blocked", "cancelled"]:
                for dependency in item["dependencies"]:
                    self.assertEqual(self.work_items[dependency]["status"], "done")

        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(work_id: str) -> None:
            if work_id in visiting:
                self.fail(f"work graph contains a cycle at {work_id}")
            if work_id in visited:
                return
            visiting.add(work_id)
            for dependency in self.work_items[work_id]["dependencies"]:
                visit(dependency)
            visiting.remove(work_id)
            visited.add(work_id)

        for work_id in work_ids:
            visit(work_id)

    def test_handoffs_preserve_role_continuity(self) -> None:
        for handoff in self.handoffs.values():
            self.assertEqual(handoff["team_id"], self.team["team_id"])
            self.assertIn(handoff["from_role_id"], self.roles)
            self.assertIn(handoff["to_role_id"], self.roles)
            self.assertTrue(set(handoff["open_items"]).issubset(self.work_items))
            self.assertTrue(set(handoff["decisions"]).issubset(self.decisions))

            if handoff["type"] == "role_succession" and handoff["status"] == "completed":
                self.assertEqual(handoff["from_role_id"], handoff["to_role_id"])
                self.assertEqual(
                    handoff["to_generation"], handoff["from_generation"] + 1
                )
                role = self.roles[handoff["to_role_id"]]
                self.assertEqual(role["binding"]["generation"], handoff["to_generation"])
                self.assertEqual(role["binding"]["agent_ref"], handoff["to_agent_ref"])
                self.assertEqual(
                    role["binding"]["predecessor_agent_ref"],
                    handoff["from_agent_ref"],
                )

    def test_decision_references_are_resolvable(self) -> None:
        known_targets = set(self.roles) | set(self.work_items)
        for decision_id, decision in self.decisions.items():
            self.assertEqual(decision["team_id"], self.team["team_id"])
            self.assertTrue(set(decision["affects"]).issubset(known_targets))
            supersedes = decision["supersedes"]
            if supersedes is not None:
                self.assertIn(supersedes, self.decisions)
                self.assertNotEqual(supersedes, decision_id)

    def test_local_markdown_links_resolve(self) -> None:
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        failures: list[str] = []

        for markdown in ROOT.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                target = target.strip().strip("<>")
                if not target or target.startswith("#") or "://" in target:
                    continue
                path_part = unquote(target.split("#", 1)[0])
                if not (markdown.parent / path_part).resolve().exists():
                    failures.append(f"{markdown.relative_to(ROOT)} -> {target}")

        self.assertEqual([], failures)

    def test_codex_skill_metadata_is_valid(self) -> None:
        skill_dir = ROOT / "skills" / "agent-teamworks"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        parts = skill_text.split("---", 2)
        self.assertEqual(len(parts), 3)
        frontmatter = yaml.safe_load(parts[1])
        self.assertEqual(frontmatter["name"], "agent-teamworks")
        self.assertIn("persistent multi-agent team", frontmatter["description"])

        openai = yaml.safe_load(
            (skill_dir / "agents" / "openai.yaml").read_text(encoding="utf-8")
        )
        interface = openai["interface"]
        self.assertEqual(interface["display_name"], "Agent Teamworks")
        self.assertIn("$agent-teamworks", interface["default_prompt"])
        self.assertLessEqual(len(interface["short_description"]), 64)

    def test_public_example_contains_no_private_project_markers(self) -> None:
        forbidden = [
            "/users/",
            "moyuan-labs",
            "commerce-kernel",
            "github.com/",
            "ghp_",
            "sk-",
        ]
        contents = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted((ROOT / "examples" / "commerce-project").rglob("*"))
            if path.is_file()
        ).lower()
        self.assertEqual([], [marker for marker in forbidden if marker in contents])


if __name__ == "__main__":
    unittest.main()
