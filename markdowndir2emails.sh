#!/bin/bash

# Default directory containing Markdown files
MARKDOWN_DIR="${1:-$HOME/Documents/markdown}"

# Python script path
PYTHON_SCRIPT="/Users/jbaty/bin/markdown2maildir.py"

# Check if directory exists
if [ ! -d "$MARKDOWN_DIR" ]; then
    echo "Directory $MARKDOWN_DIR does not exist."
    exit 1
fi

# Process each Markdown file recursively
find "$MARKDOWN_DIR" -type f -name "*.md" | while read -r file; do
    echo "Processing: $file"
    python "$PYTHON_SCRIPT" "$file"
done

echo "All Markdown files processed."
