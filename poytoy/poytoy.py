#!/usr/bin/env python3

import sys
import subprocess
import tomllib
from pathlib import Path


def find_project(name: str) -> Path:
    path = Path(name)
    if not path.exists():
        print(f"Project '{name}' not found.")
        sys.exit(1)
    return path


def load_config(project_path: Path) -> dict:
    config_path = project_path / "poytoy.toml"
    if not config_path.exists():
        print("Missing poytoy.toml")
        sys.exit(1)

    with config_path.open("rb") as f:
        return tomllib.load(f)


def run_command(cmd: str, cwd: Path):
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        sys.exit(130)


def main():
    if len(sys.argv) < 3:
        print("Usage: poytoy <sync|make|run> <project>")
        sys.exit(1)

    action = sys.argv[1]
    project_name = sys.argv[2]

    project_path = find_project(project_name)
    config = load_config(project_path)

    if action not in config:
        print(f"No '{action}' section defined in poytoy.toml")
        sys.exit(1)

    cmd = config[action].get("cmd")
    if not cmd:
        print(f"No command defined for '{action}'")
        sys.exit(1)

    run_command(cmd, project_path)


if __name__ == "__main__":
    main()
