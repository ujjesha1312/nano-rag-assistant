import glob
from pathlib import Path

def load_knowledge():
    knowledge = {}

    files = glob.glob("knowledge-base/employees/*.txt")

    for file in files:
        key = Path(file).stem.lower()
        with open(file, "r", encoding="utf-8") as f:
            knowledge[key] = f.read()

    return knowledge
