from pathlib import Path
import shutil
import hashlib
import random

PROJECT_DIR = Path(__file__).resolve().parent.parent

# Original CASIA 2 dataset
CASIA_DIR = Path.home() / "Downloads" / "archive" / "CASIA2"

REAL_SOURCE = CASIA_DIR / "Au"
FAKE_SOURCE = CASIA_DIR / "Tp"

# Existing training/validation dataset
REAL_USED = PROJECT_DIR / "dataset" / "real"
FAKE_USED = PROJECT_DIR / "dataset" / "fake"

# New unseen test dataset
TEST_REAL = PROJECT_DIR / "dataset" / "test" / "real"
TEST_FAKE = PROJECT_DIR / "dataset" / "test" / "fake"

NUM_TEST_IMAGES = 500

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}

TEST_REAL.mkdir(parents=True, exist_ok=True)
TEST_FAKE.mkdir(parents=True, exist_ok=True)


def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def get_used_hashes(folder):
    hashes = set()

    for image in folder.iterdir():
        if image.is_file() and image.suffix.lower() in IMAGE_EXTENSIONS:
            try:
                hashes.add(file_hash(image))
            except:
                pass

    return hashes


print("Checking images already used...")

used_real = get_used_hashes(REAL_USED)
used_fake = get_used_hashes(FAKE_USED)

print("Used real images:", len(used_real))
print("Used fake images:", len(used_fake))


def get_unused_images(source, used_hashes):
    available = []

    for image in source.iterdir():
        if image.is_file() and image.suffix.lower() in IMAGE_EXTENSIONS:
            try:
                if file_hash(image) not in used_hashes:
                    available.append(image)
            except:
                pass

    return available


real_available = get_unused_images(REAL_SOURCE, used_real)
fake_available = get_unused_images(FAKE_SOURCE, used_fake)

random.seed(42)

random.shuffle(real_available)
random.shuffle(fake_available)

real_test = real_available[:NUM_TEST_IMAGES]
fake_test = fake_available[:NUM_TEST_IMAGES]


print("\nUnseen test images selected:")
print("Real:", len(real_test))
print("Fake:", len(fake_test))


for i, image in enumerate(real_test, 1):
    destination = TEST_REAL / f"real_{i:04d}{image.suffix.lower()}"
    shutil.copy2(image, destination)


for i, image in enumerate(fake_test, 1):
    destination = TEST_FAKE / f"fake_{i:04d}{image.suffix.lower()}"
    shutil.copy2(image, destination)


print("\nUnseen test dataset created successfully!")
print("Test real images:", len(real_test))
print("Test fake images:", len(fake_test))
print("Test dataset:", PROJECT_DIR / "dataset" / "test")