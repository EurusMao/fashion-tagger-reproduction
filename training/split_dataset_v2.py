from pathlib import Path
from collections import Counter
import csv
import random

ROOT = Path.cwd()
DATA_DIR = ROOT / "data" / "processed"
SOURCE = DATA_DIR / "labels_v2.csv"

random.seed(42)

with SOURCE.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

by_class = {}
for row in rows:
    by_class.setdefault(row["label"], []).append(row)

splits = {"train": [], "validation": [], "test": []}

for label, items in sorted(by_class.items()):
    random.shuffle(items)
    n = len(items)
    n_train = int(n * 0.70)
    n_val = int(n * 0.15)

    splits["train"].extend(items[:n_train])
    splits["validation"].extend(items[n_train:n_train + n_val])
    splits["test"].extend(items[n_train + n_val:])

for split_name, items in splits.items():
    random.shuffle(items)
    output = DATA_DIR / f"{split_name}_v2.csv"

    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "filename", "label", "original_category", "item_ID"
            ]
        )
        writer.writeheader()
        writer.writerows(items)

    print(f"\n{split_name.upper()}: {len(items)} images")
    print("Class counts:", dict(sorted(
        Counter(row["label"] for row in items).items()
    )))
    print("Saved:", output)

print("\nVersion 2 split complete.")
