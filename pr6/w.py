from pathlib import Path

file_path = Path("example.txt")

with file_path.open("w") as f:
    f.write("Hello, world!\n")
    f.write("This is a file\n")

print()



