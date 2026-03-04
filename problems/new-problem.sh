#!/bin/bash
# Create a new problem from template
# Usage: ./new-problem.sh <problem-name>
# Example: ./new-problem.sh dpv_3.4

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <problem-name>"
    echo "Example: $0 dpv_3.4"
    exit 1
fi

PROBLEM_NAME="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROBLEM_DIR="$SCRIPT_DIR/$PROBLEM_NAME"
TEMPLATE_FILE="$SCRIPT_DIR/template.py"

if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Error: Template file not found at $TEMPLATE_FILE"
    exit 1
fi

if [ -d "$PROBLEM_DIR" ]; then
    echo "Error: Problem directory '$PROBLEM_NAME' already exists"
    exit 1
fi

echo "Creating new problem '$PROBLEM_NAME'..."

# Create problem directory
mkdir -p "$PROBLEM_DIR"

# Copy template and rename
cp "$TEMPLATE_FILE" "$PROBLEM_DIR/${PROBLEM_NAME}.py"
chmod +x "$PROBLEM_DIR/${PROBLEM_NAME}.py"

echo "✓ Created $PROBLEM_DIR/"
echo "  - ${PROBLEM_NAME}.py"
echo ""
echo "Next steps:"
echo "  1. Edit $PROBLEM_DIR/${PROBLEM_NAME}.py"
echo "  2. Add problem description, tests, and implementation"
echo "  3. Run: ./dispense-problem.sh $PROBLEM_NAME"
