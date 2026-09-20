from pathlib import Path
import shutil
import random

# Project folder
PROJECT_DIR = Path(__file__).resolve().parent

# Original CASIA 2 dataset
CASIA_DIR = Path.home() / "Downloads" / "archive" / "CASIA2"

# Source folders
REAL_SOURCE = CASIA_DIR / "Au"
FAKE_SOURCE = CASIA_DIR / "Tp"

# Destination folders
REAL_DEST = PROJECT_DIR / "dataset" / "real"
FAKE_DEST = PROJECT_DIR / "dataset" / "fake"

# Number of images to use
NUM_IMAGES = 1500

# Supported image formats
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}

# Create destination folders
REAL_DEST.mkdir(parents=True, exist_ok=True)
FAKE_DEST.mkdir(parents=True, exist_ok=True)

# Get image files
real_images = [
    f for f in REAL_SOURCE.iterdir()
    if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
]

fake_images = [
    f for f in FAKE_SOURCE.iterdir()
    if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
]

# Random selection
random.seed(42)

real_images = random.sample(real_images, min(NUM_IMAGES, len(real_images)))
fake_images = random.sample(fake_images, min(NUM_IMAGES, len(fake_images)))

print(f"Real images selected: {len(real_images)}")
print(f"Fake images selected: {len(fake_images)}")

# Copy real images
for i, image in enumerate(real_images, 1):
    destination = REAL_DEST / f"real_{i:04d}{image.suffix.lower()}"
    shutil.copy2(image, destination)

# Copy fake images
for i, image in enumerate(fake_images, 1):
    destination = FAKE_DEST / f"fake_{i:04d}{image.suffix.lower()}"
    shutil.copy2(image, destination)

print("\nDataset preparation completed!")
print(f"Real images: {len(real_images)}")
print(f"Fake images: {len(fake_images)}")
print(f"Dataset location: {PROJECT_DIR / 'dataset'}")