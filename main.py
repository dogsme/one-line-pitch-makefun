#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt."""
import os

SENTENCE = "Just describe your app idea in plain words and I'll have an AI agent build you a working first version on make.fun today, free to try, no coding needed, and yours to keep."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
