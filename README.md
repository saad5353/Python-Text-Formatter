# Text Alignment Formatter

A Python script that formats plain text files with configurable alignment and line width options.

## Overview

This script reads any plain text file and generates formatted versions with different text alignments:
- Left-aligned text
- Justified text (both left and right margins aligned)

The script processes the input text while preserving paragraph structure and adds metadata headers to each output file.

## Files

| File | Description |
|------|-------------|
| `align.py` | Main Python script that performs the text formatting |
| Input text file | Any plain text file to be formatted (specify in the script) |

## Features

- **Left Alignment**: Standard text wrapping with left-aligned margins using customizable width
- **Justified Alignment**: Evenly spaced text with both left and right margins aligned
- **Configurable Width**: Easily modify line width (default: 40 and 70 characters)
- **Paragraph Preservation**: Original paragraph breaks are maintained
- **Metadata Headers**: Each output file includes information about the formatting applied

## Requirements

- Python 3.x
- No external libraries required (uses only standard library `textwrap`)

## Configuration

Edit the script to specify:
- Input file path (currently set to `"KantWhatIsEnlightenment.txt"`)
- Desired line widths (currently set to 40 and 70 characters)
- Output file naming convention

## Usage

1. Place your input text file in the same directory as the script
2. Update the input filename in the script:
   ```python
   file = open("your-file.txt", "r")
