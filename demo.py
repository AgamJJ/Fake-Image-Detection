import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

import torch
import torch.nn as nn
from torchvision import models, transforms


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "fake_image_resnet18.pth"
)


# ============================================================
# DEVICE
# ============================================================

device = torch.device("cpu")


# ============================================================
# LOAD MODEL
# ============================================================

checkpoint = torch.load(
    MODEL_PATH,
    map_location=device
)

classes = checkpoint.get("classes", ["fake", "real"])
image_size = checkpoint.get("image_size", 224)


model = models.resnet18(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    len(classes)
)

model.load_state_dict(checkpoint["model_state_dict"])

model = model.to(device)
model.eval()


# ============================================================
# IMAGE TRANSFORM
# ============================================================

transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Fake Image Detection")

root.geometry("700x850")

root.configure(bg="white")


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="FAKE IMAGE DETECTION",
    font=("Arial", 28, "bold"),
    bg="white",
    fg="black"
)

title_label.pack(pady=(30, 10))


# ============================================================
# SUBTITLE
# ============================================================

subtitle_label = tk.Label(
    root,
    text="Deep Learning Based Image Authenticity Detection",
    font=("Arial", 14),
    bg="white",
    fg="gray"
)

subtitle_label.pack(pady=(0, 25))


# ============================================================
# IMAGE AREA
# ============================================================

image_label = tk.Label(
    root,
    text="No image selected",
    font=("Arial", 16),
    bg="white",
    fg="gray"
)

image_label.pack(pady=10)


# ============================================================
# PREDICTION LABEL
# ============================================================

prediction_label = tk.Label(
    root,
    text="Prediction: --",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="black"
)

prediction_label.pack(pady=(20, 10))


# ============================================================
# CONFIDENCE LABEL
# ============================================================

confidence_label = tk.Label(
    root,
    text="Confidence: --",
    font=("Arial", 16),
    bg="white",
    fg="black"
)

confidence_label.pack(pady=5)


# ============================================================
# SELECT IMAGE FUNCTION
# ============================================================

def select_image():

    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:

        # ----------------------------------------------------
        # DISPLAY IMAGE
        # ----------------------------------------------------

        image = Image.open(file_path).convert("RGB")

        display_image = image.copy()

        display_image.thumbnail((500, 500))

        photo = ImageTk.PhotoImage(display_image)

        image_label.config(
            image=photo,
            text=""
        )

        image_label.image = photo


        # ----------------------------------------------------
        # PREPROCESS IMAGE
        # ----------------------------------------------------

        input_tensor = transform(image)

        input_tensor = input_tensor.unsqueeze(0)

        input_tensor = input_tensor.to(device)


        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        with torch.no_grad():

            output = model(input_tensor)

            probabilities = torch.softmax(
                output,
                dim=1
            )

            predicted_class = torch.argmax(
                probabilities,
                dim=1
            ).item()

            confidence = probabilities[
                0,
                predicted_class
            ].item() * 100


        # ----------------------------------------------------
        # GET CLASS NAME
        # ----------------------------------------------------

        prediction = classes[predicted_class].upper()


        # ----------------------------------------------------
        # UPDATE PREDICTION
        # ----------------------------------------------------

        prediction_label.config(
            text=f"Prediction: {prediction}"
        )


        # ----------------------------------------------------
        # UPDATE CONFIDENCE
        # ----------------------------------------------------

        confidence_label.config(
            text=f"Confidence: {confidence:.2f}%"
        )


    except Exception as e:

        prediction_label.config(
            text="Prediction: Error"
        )

        confidence_label.config(
            text=f"Error: {str(e)}"
        )


# ============================================================
# SELECT IMAGE BUTTON
# ============================================================

select_button = tk.Button(
    root,
    text="SELECT IMAGE",
    command=select_image,
    font=("Arial", 16, "bold"),
    padx=30,
    pady=12,
    bg="white",
    fg="black",
    relief="solid",
    bd=1,
    cursor="hand2"
)

select_button.pack(pady=20)


# ============================================================
# FOOTER
# ============================================================

footer_label = tk.Label(
    root,
    text="PyTorch • ResNet18 • Computer Vision",
    font=("Arial", 10),
    bg="white",
    fg="gray"
)

footer_label.pack(
    side="bottom",
    pady=25
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
