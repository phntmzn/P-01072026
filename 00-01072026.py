import os
import re

def create_markdown_files(
    count,
    output_dir="EVASIVE MALWARE",
    date_str="01072026",
    zero_pad=2
):
    os.makedirs(output_dir, exist_ok=True)

    pattern = re.compile(rf"(\d+)-{date_str}\.md")

    existing_indices = []

    for name in os.listdir(output_dir):
        match = pattern.fullmatch(name)
        if match:
            existing_indices.append(int(match.group(1)))

    start_index = max(existing_indices) + 1 if existing_indices else 0

    for i in range(start_index, start_index + count):
        index = str(i).zfill(zero_pad)
        filename = f"{index}-{date_str}.md"
        path = os.path.join(output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {index}-{date_str}\n")

    print(f"Added {count} markdown files starting at {str(start_index).zfill(zero_pad)}")

if __name__ == "__main__":
    create_markdown_files(10)
