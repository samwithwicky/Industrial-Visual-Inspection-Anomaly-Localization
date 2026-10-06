from pathlib import Path

DATASET_DIR = Path("data/raw/bottle")

train_dir = DATASET_DIR / "train"
test_dir = DATASET_DIR / "test"
ground_truth_dir = DATASET_DIR / "ground_truth"


# Check required directories
paths = {
    "dataset": DATASET_DIR,
    "train": train_dir,
    "test": test_dir,
    "ground_truth": ground_truth_dir,
}

print("Path validation:")

for name, path in paths.items():
    status = "OK" if path.exists() else "MISSING"
    print(f"{name}: {path} -> {status}")


# Count PNG images
def count_images(directory):
    return len(list(directory.glob("*.png")))


print("\nTraining images:")
print("good:", count_images(train_dir / "good"))


print("\nTest images:")

for defect_type in sorted(test_dir.iterdir()):
    if defect_type.is_dir():
        print(
            defect_type.name,
            ":",
            count_images(defect_type)
        )


print("\nGround-truth masks:")

for defect_type in sorted(ground_truth_dir.iterdir()):
    if defect_type.is_dir():
        print(
            defect_type.name,
            ":",
            count_images(defect_type)
        )