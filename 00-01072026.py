import os

def create_markdown_files(
    count,
    output_dir="markdown_files",
    prefix="note",
    start_index=1
):
    os.makedirs(output_dir, exist_ok=True)

    for i in range(start_index, start_index + count):
        filename = f"{prefix}_{i}.md"
        path = os.path.join(output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            pass  # creates empty file

    print(f"Created {count} markdown files in '{output_dir}'")

if __name__ == "__main__":
    create_markdown_files(10)
