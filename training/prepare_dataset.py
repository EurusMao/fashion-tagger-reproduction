from collections import Counter
from pathlib import Path
from io import BytesIO
import csv
import time

from datasets import load_dataset
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR = ROOT / "data" / "processed" / "images"
CSV_PATH = ROOT / "data" / "processed" / "labels.csv"

TARGET_PER_CLASS = 200
MAX_RECORDS = 10000
IMAGE_SIZE = (128, 128)

CLASSES = ["top", "bottom", "dress", "outerwear", "other"]
counts = Counter()
rows = []
scanned = 0
failed = 0

def map_category(category):
    if not category:
        return None

    c = category.lower()

    # Dresses and jumpsuits
    if any(x in c for x in [
        "dress", "jumpsuit", "romper", "overall"
    ]):
        return "dress"

    # Bottoms
    if any(x in c for x in [
        "jeans", "pants", "trousers", "shorts",
        "skirts", "leggings", "bottoms"
    ]):
        return "bottom"

    # Outerwear
    if any(x in c for x in [
        "jacket", "coat", "blazer", "outerwear",
        "trench", "parka"
    ]):
        return "outerwear"

    # Tops
    if any(x in c for x in [
        "blouse", "t-shirt", "t shirt", "tee",
        "shirt", "tank top", "crop top", "tops",
        "sweater", "hoodie", "sweatshirt"
    ]):
        return "top"

    # Only explicitly recognizable miscellaneous categories
    if any(x in c for x in [
        "shoe", "sandal", "boot", "sneaker",
        "handbag", "bag", "accessor", "jewelry",
        "scarf", "hat", "belt", "sunglasses",
        "swimsuit", "swimwear", "lingerie",
        "underwear", "sleepwear", "nightgown"
    ]):
        return "other"

    return None

def get_pil_image(value):
    if isinstance(value, Image.Image):
        return value.convert("RGB")

    if isinstance(value, dict):
        if value.get("bytes"):
            return Image.open(BytesIO(value["bytes"])).convert("RGB")
        if value.get("path"):
            return Image.open(value["path"]).convert("RGB")

    raise ValueError("Unsupported image format")

def main():
    global scanned, failed

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    print("Connecting to iMaterialist using streaming...")
    ds = load_dataset(
        "Marqo/iMaterialist",
        split="data",
        streaming=True
    )

    started = time.time()

    for item in ds:
        scanned += 1

        category = item.get("category")
        label = map_category(category)

        if label is None or counts[label] >= TARGET_PER_CLASS:
            if scanned >= MAX_RECORDS:
                break
            continue

        try:
            image = get_pil_image(item["image"])
            image.thumbnail(IMAGE_SIZE)

            # Put each image on a fixed-size white canvas
            canvas = Image.new("RGB", IMAGE_SIZE, "white")
            x = (IMAGE_SIZE[0] - image.width) // 2
            y = (IMAGE_SIZE[1] - image.height) // 2
            canvas.paste(image, (x, y))

            filename = f"{label}_{counts[label]:04d}.jpg"
            canvas.save(IMAGE_DIR / filename, "JPEG", quality=85)

            rows.append({
                "filename": filename,
                "label": label,
                "original_category": category,
                "item_ID": item.get("item_ID", "")
            })
            counts[label] += 1

            if sum(counts.values()) % 50 == 0:
                print(
                    f"Scanned {scanned}; saved {sum(counts.values())}; "
                    f"class counts: {dict(counts)}"
                )

        except Exception as exc:
            failed += 1
            if failed <= 5:
                print("Skipped an unreadable image:", str(exc)[:150])

        if all(counts[c] >= TARGET_PER_CLASS for c in CLASSES):
            break

        if scanned >= MAX_RECORDS:
            break

    with CSV_PATH.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["filename", "label", "original_category", "item_ID"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print("\nPreparation finished.")
    print("Records scanned:", scanned)
    print("Images saved:", len(rows))
    print("Unreadable images skipped:", failed)
    print("Class counts:", dict(counts))
    print("Labels file:", CSV_PATH)
    print("Image folder:", IMAGE_DIR)
    print("Elapsed seconds:", round(time.time() - started, 1))

    if len(rows) < 1000:
        print(
            "\nNote: fewer than 1000 images were collected. "
            "Review class counts before deciding whether to scan more."
        )

if __name__ == "__main__":
    main()
