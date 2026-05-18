#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[2]
required = ["AGENT_RULES.md", "AGENTS.md"]
missing = [name for name in required if not (root / name).exists()]

if missing:
    sys.stderr.write(f"Missing recommended files: {', '.join(missing)}\n")
    sys.exit(0)

sys.exit(0)
