from pathlib import Path

text = Path("./text.txt").read_text()
print(text)
