import os

def create_markdown_files(
    count,
    output_dir="EVASIVE MALWARE",
    date_str="01072026",
    start_index=0,
    zero_pad=2
):
    os.makedirs(output_dir, exist_ok=True)

    for i in range(start_index, start_index + count):
        index = str(i).zfill(zero_pad)
        filename = f"{index}-{date_str}.md"
        path = os.path.join(output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {index}-{date_str}\n")

    print(f"Created {count} markdown files in '{output_dir}'")

if __name__ == "__main__":
    create_markdown_files(10)
