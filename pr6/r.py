from pathlib import Path

file_path = Path("example.txt")

with file_path.open("r") as f:
    content = f.read()
    print("Full content:\n", content)
