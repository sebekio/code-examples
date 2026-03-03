#!/usr/bin/env bash
# scripts/run-py.sh
# Runs a Python file using the workspace container's Python.
# Called by VS Code task: "Run Current File (Python)"
#
# Usage: ./scripts/run-py.sh <file.py>
#        VS Code passes ${file} automatically.

set -euo pipefail

FILE="${1:-}"

if [[ -z "$FILE" ]]; then
  echo "Usage: run-py.sh <file.py>" >&2
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
  echo "File not found: $FILE" >&2
  exit 1
fi

echo "── run: $(basename "$FILE") ──────────────────────────────────"
python3 "$FILE"
echo "── done ──────────────────────────────────────────────────────"
