#!/usr/bin/env python3
"""Build a self-contained Codex marketplace from the canonical plugin sources."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_PATHS = (
    ".codex-plugin/plugin.json",
    "README.md",
    "README.zh-CN.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "requirements-dev.txt",
    "framework",
    "roles",
    "protocols",
    "schemas",
    "adapters",
    "skills",
    "examples",
    "docs",
    "evals",
    "scripts",
    "tests",
)


def build(output: Path) -> Path:
    output = output.expanduser().resolve()
    # A fresh destination avoids deleting user files or retaining stale releases.
    if output.exists():
        raise ValueError(f"Output already exists: {output}. Choose a fresh directory.")
    for entry in PACKAGE_PATHS:
        source = ROOT / entry
        if not source.exists():
            raise ValueError(f"Missing package source: {entry}")
        if source.is_dir() and output.is_relative_to(source):
            raise ValueError(f"Output must not be inside package source: {entry}")

    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    plugin_name = manifest["name"]
    if plugin_name != "agent-teamworks":
        raise ValueError("This builder packages the agent-teamworks plugin.")
    plugin_root = output / "plugins" / plugin_name
    plugin_root.mkdir(parents=True)
    for entry in PACKAGE_PATHS:
        source = ROOT / entry
        destination = plugin_root / entry
        if source.is_dir():
            shutil.copytree(
                source,
                destination,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
            )
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    marketplace = {
        "name": "agent-teamworks",
        "interface": {"displayName": "Agent Teamworks"},
        "plugins": [{
            "name": plugin_name,
            "source": {"source": "local", "path": f"./plugins/{plugin_name}"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Productivity",
        }],
    }
    marketplace_path = output / ".agents" / "plugins" / "marketplace.json"
    marketplace_path.parent.mkdir(parents=True)
    marketplace_path.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")
    return plugin_root


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=ROOT / "dist",
        help="Fresh marketplace directory (default: repository dist/).",
    )
    args = parser.parse_args()
    try:
        plugin_root = build(args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")
    print(f"Marketplace: {plugin_root.parent.parent}")
    print(f"Plugin: {plugin_root}")
    print("Build complete. No Codex installation or configuration was changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
