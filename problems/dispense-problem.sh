#!/bin/bash
# Dispense a problem to student folders (jason and trajan)
# Usage: ./dispense-problem.sh <problem-dir>
# Example: ./dispense-problem.sh dpv_3.3

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <problem-dir>"
    echo "Example: $0 dpv_3.3"
    exit 1
fi

PROBLEM_DIR="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JASON_DIR="$SCRIPT_DIR/../jason"
TRAJAN_DIR="$SCRIPT_DIR/../trajan"

if [ ! -d "$SCRIPT_DIR/$PROBLEM_DIR" ]; then
    echo "Error: Problem directory '$PROBLEM_DIR' not found in $SCRIPT_DIR"
    exit 1
fi

echo "Dispensing problem '$PROBLEM_DIR' to student folders..."

# Copy to jason
echo "  → Copying to jason/$PROBLEM_DIR/"
cp -r "$SCRIPT_DIR/$PROBLEM_DIR" "$JASON_DIR/"

# Copy to trajan
echo "  → Copying to trajan/$PROBLEM_DIR/"
cp -r "$SCRIPT_DIR/$PROBLEM_DIR" "$TRAJAN_DIR/"

echo "✓ Done! Problem dispensed to both jason and trajan folders."
