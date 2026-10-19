from pathlib import Path
from collections import Counter
import csv

ROOT = Path.cwd()
DATA_DIR = ROOT / "data" / "processed"
IMAGE_DIR = DATA_DIR / "images"

SOURCE = DATA_DIR / "labels.csv"
OUTPUT = DATA_DIR / "labels_v2.csv"

def map_category(category):
    if not category:
        return None

    c = category.lower().strip()

    # Explicit corrections first
    if c == "petticoats":
        return None

    if c == "dress shirts":
        return "top"

    # Dresses and one-piece outfits
    if any(x in c for x in [
        "dress", "jumpsuit", "romper", "overall"
    ]):
        return "dress"

    # Bottoms
    if any(x in c for x in [
        "jeans", "pants", "trousers", "shorts",
        "skirts", "leggings", "bottoms", "capri"
    ]):
        return "bottom"

    # Outerwear
    if any(x in c for x in [
        "jacket", "coat", "blazer", "outerwear",
        "trench", "parka", "peacoat"
    ]):
        return "outerwear"

    # Tops
    if any(x in c for x in [
        "blouse", "t-shirt", "t shirt", "tee",
        "shirt", "tank top", "crop top", "tops",
        "sweater", "hoodie", "sweatshirt", "tube top"
    ]):
        return "top"

    # Other recognizable apparel and footwear
    if any(x in c for x in [
        "shoe", "sandal", "boot", "sneaker",
        "handbag", "bag", "accessor", "jewelry",
        "scarf", "hat", "belt", "sunglasses",
        "swimsuit", "swimwear", "lingerie",
        "underwear", "sleepwear", "nightgown",
        "swimwear", "cover-up"
    ]):
        return "other"

    return None


with SOURCE.open(encoding="utf-8-sig", newline="") as f:
    original_rows = list(csv.DictReader(f))

new_rows = []
counts = Counter()
excluded = Counter()

for row in original_rows:
    category = row.get("original_category", "")
    label = map_category(category)

    if label is None:
        excluded[category or "(missing category)"] += 1
        continue

    if not (IMAGE_DIR / row["filename"]).is_file():
        excluded["missing image file"] += 1
        continue

    new_rows.append({
        "filename": row["filename"],
        "label": label,
        "original_category": category,
        "item_ID": row.get("item_ID", "")
    })
    counts[label] += 1

with OUTPUT.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "filename", "label", "original_category", "item_ID"
        ]
    )
    writer.writeheader()
    writer.writerows(new_rows)

print("Version 2 labels created.")
print("Images retained:", len(new_rows))
print("Class counts:", dict(sorted(counts.items())))
print("Excluded records:", sum(excluded.values()))
print("Excluded categories:", dict(excluded))
print("Output:", OUTPUT)
print("Original labels.csv was not changed.")
