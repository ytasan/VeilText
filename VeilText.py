"""
VeilText
Author: ytasan 
Last Updated: 2026-02-11
Description: Selective line-based text masking tool that preserves indentation and formatting.
"""

import re


def mask_word(word):
    if len(word) == 3:
        return "..."
    elif len(word) == 4:
        return "...."
    elif len(word) < 3:
        return word
    else:
        return word[0] + "." * (len(word) - 2) + word[-1]


def mask_text(text):
    parts = re.split(r'(\s+)', text)
    masked_parts = [
        mask_word(part) if not part.isspace() else part
        for part in parts
    ]
    return "".join(masked_parts)


if __name__ == "__main__":
    input_file = "VeilText.input"
    output_file = "VeilText.output"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        output_lines = []
        for line in lines:
            line = line.rstrip("\n")

            if line.lstrip().startswith("*"):
                star_index = line.find("*")
                content = line[star_index + 1:]
                output_lines.append(mask_text(content))
            else:
                output_lines.append(line)

        with open(output_file, "w", encoding="utf-8") as f:
            for line in output_lines:
                f.write(line + "\n")

        print(f"Masked content has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")