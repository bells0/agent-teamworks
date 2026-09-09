from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]


class PluginDistribution(unittest.TestCase):
    def test_built_marketplace_is_self_contained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "marketplace"
            subprocess.run(
                [sys.executable, str(ROOT / "scripts/build_plugin.py"), "--output", str(output)],
                check=True, capture_output=True, text=True,
            )
            marketplace = json.loads(
                (output / ".agents/plugins/marketplace.json").read_text(encoding="utf-8")
            )
            entry, = marketplace["plugins"]
            plugin = (output / entry["source"]["path"]).resolve()
            self.assertTrue(plugin.is_relative_to(output.resolve()))
            manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["name"], entry["name"])
            self.assertEqual(manifest["name"], plugin.name)
            self.assertEqual(entry["policy"]["installation"], "AVAILABLE")
            self.assertEqual(entry["policy"]["authentication"], "ON_INSTALL")
            self.assertEqual(entry["category"], "Productivity")
            self.assertTrue((plugin / manifest["skills"] / "agent-teamworks/SKILL.md").is_file())
            self.assertEqual(3, len(manifest["interface"]["defaultPrompt"]))

            # Resolve links from the copied package, not the developer checkout.
            links = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
            for markdown in plugin.rglob("*.md"):
                for target in links.findall(markdown.read_text(encoding="utf-8")):
                    target = target.strip().strip("<>")
                    if not target or target.startswith("#") or "://" in target:
                        continue
                    resolved = (markdown.parent / unquote(target.split("#", 1)[0])).resolve()
                    with self.subTest(file=str(markdown.relative_to(plugin)), target=target):
                        self.assertTrue(resolved.is_relative_to(plugin), "Link escapes plugin")
                        self.assertTrue(resolved.exists(), "Missing bundled reference")

            self.assertFalse((plugin / ".git").exists())
            self.assertFalse((plugin / ".agent-teamworks").exists())
            self.assertFalse((plugin / "dist").exists())
            for path in plugin.rglob("*"):
                if path.is_file():
                    self.assertEqual(path.read_bytes(), (ROOT / path.relative_to(plugin)).read_bytes())

    def test_existing_output_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            marker = output / "keep.txt"
            marker.write_text("existing content", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/build_plugin.py"), "--output", str(output)],
                capture_output=True, text=True,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("Output already exists", result.stderr)
            self.assertEqual("existing content", marker.read_text(encoding="utf-8"))
            self.assertEqual([marker], list(output.iterdir()))


if __name__ == "__main__":
    unittest.main()
