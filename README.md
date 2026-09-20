# Fake Image Detection Using Deep Learning and Computer Vision

A Deep Learning and Computer Vision based system that classifies an input image as REAL or FAKE using Transfer Learning with ResNet18.

## Project Overview

Image manipulation has become easier with modern image editing tools. Detecting whether an image is authentic or manipulated is an important application of Computer Vision and Deep Learning.

This project uses a ResNet18 Convolutional Neural Network with Transfer Learning to learn visual patterns from authentic and manipulated images.

The system takes an image as input, preprocesses it, passes it through the trained model, and displays the predicted class along with a confidence score.

Project Pipeline:

Input Image → Preprocessing → ResNet18 → Classification → REAL / FAKE → Confidence Score

Note: The model is trained on the CASIA 2.0 dataset and is intended for educational and experimental purposes. It should not be considered a universal detector for every type of manipulated or AI-generated image.

## Objectives

- Detect authentic and manipulated images using Deep Learning.
- Apply image preprocessing and augmentation.
- Use Transfer Learning for image classification.
- Implement ResNet18 using PyTorch.
- Train a binary image classification model.
- Evaluate the model using a separate unseen test dataset.
- Develop a simple graphical user interface.
- Display the prediction and confidence score.

## Technologies Used

- Python
- PyTorch
- Torchvision
- OpenCV
- Pillow (PIL)
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Tkinter
- VS Code

## Dataset

The project uses the CASIA 2.0 Image Tampering Detection Dataset.

The dataset contains authentic and manipulated/tampered images.

For this project, the images were organized into two classes:

- Real – authentic/original images
- Fake – manipulated/tampered images

Training Dataset:
- Real: 1500 images
- Fake: 1500 images
- Total: 3000 images

Unseen Test Dataset:
- Real: 500 images
- Fake: 500 images
- Total: 1000 images

The test images were kept separate from the training data for final evaluation.

## Dataset Structure

dataset/
├── real/
├── fake/
└── test/
    ├── real/
    └── fake/

## Model

The project uses ResNet18 with Transfer Learning.

ResNet18 is a Convolutional Neural Network architecture based on residual learning. A pretrained ResNet18 architecture was adapted for binary classification by replacing its final fully connected layer.

Model:

Pretrained ResNet18
        ↓
Feature Extraction
        ↓
Modified Fully Connected Layer
        ↓
Fake / Real

Model Configuration:

- Architecture: ResNet18
- Framework: PyTorch
- Number of Classes: 2
- Classes: Fake and Real
- Input Image Size: 224 × 224
- Device: CPU

The trained model is saved as:

models/fake_image_resnet18.pth

## Image Preprocessing

Before an image is passed to the model, it is preprocessed according to the model input requirements.

The main preprocessing steps include:

- Resize image to 224 × 224
- Convert image to Tensor
- Normalize image using ImageNet mean and standard deviation

Data augmentation was also applied during training to improve model generalization.

## Training

The model was trained using PyTorch.

Training Configuration:

- Model: ResNet18
- Image Size: 224 × 224
- Batch Size: 16
- Learning Rate: 0.0001
- Optimizer: Adam
- Epochs: 10
- Device: CPU
- Number of Classes: 2

Training Results:

- Best Validation Accuracy: 81.75%
- Final Training Accuracy: 96.85%

The difference between training and validation performance indicates that the model learned the training data strongly, while its performance on unseen data was lower.

## Model Evaluation

After training, the model was evaluated on a separate unseen test dataset containing 1000 images.

Final Test Accuracy:

66.50%

Classification Report:

Class        Precision    Recall    F1-Score
Fake           0.80        0.44       0.57
Real           0.61        0.89       0.73

Confusion Matrix:

                 Predicted
              Fake      Real

Actual Fake    222       278
Actual Real     57       443

The evaluation shows that the model can classify authentic and manipulated images, but false positives and false negatives are still present.

## Graphical User Interface

A simple desktop GUI was developed using Tkinter.

The application allows the user to:

1. Select an image from the computer.
2. Display the selected image.
3. Preprocess the image.
4. Run the trained ResNet18 model.
5. Display the prediction.
6. Display the confidence score.

Example prediction:

Prediction: REAL
Confidence: 96.44%

Example fake prediction:

Prediction: FAKE
Confidence: 97.85%

The GUI implementation is located in:

app/demo.py

## Project Structure

Fake_Image_Detection/
│
├── app/
│   ├── demo.py
│   ├── evaluate.py
│   └── prepare_test.py
│
├── dataset/
│   ├── real/
│   ├── fake/
│   └── test/
│       ├── real/
│       └── fake/
│
├── models/
│   └── fake_image_resnet18.pth
│
├── results/
│   └── correct_confusion_matrix.png
│
├── prepare_dataset.py
│
└── README.md

Note: The venv folder is used only for the local Python environment and should not be uploaded to GitHub.

## Installation

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/Fake_Image_Detection.git

cd Fake_Image_Detection

Replace YOUR_USERNAME with your GitHub username.

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Virtual Environment

For Windows PowerShell:

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

venv\Scripts\activate

### 4. Install Dependencies

pip install torch torchvision

pip install opencv-python pillow numpy matplotlib scikit-learn tqdm seaborn

## Running the Application

After installing the required dependencies, run:

python app/demo.py

The Tkinter GUI will open.

Select an image and the application will display:

Prediction: REAL / FAKE
Confidence: XX.XX%

## Model Evaluation

To evaluate the trained model on the unseen test dataset, run:

python app/evaluate.py

The evaluation script provides:

- Test Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Results Summary

Training Images: 3000
Test Images: 1000
Training Epochs: 10
Best Validation Accuracy: 81.75%
Final Training Accuracy: 96.85%
Final Test Accuracy: 66.50%
Model: ResNet18
Framework: PyTorch
Image Size: 224 × 224
Device: CPU

## Limitations

- The model is trained using the CASIA 2.0 dataset.
- Performance can vary on images from different datasets and sources.
- The model can produce false positives and false negatives.
- Image compression and resizing may affect predictions.
- The current test accuracy is 66.50%, so further improvement is possible.
- The system is not a universal image-forgery detector.
- The model was not specifically trained to detect every type of AI-generated image.

## Future Scope

The project can be improved by:

- Using larger and more diverse datasets.
- Applying stronger data augmentation techniques.
- Experimenting with architectures such as EfficientNet and Xception.
- Using advanced image-forensics techniques.
- Detecting and highlighting manipulated regions.
- Adding batch image analysis.
- Improving real-world generalization.
- Developing a web-based interface.
- Adding specialized detection methods for AI-generated images.

## Learning Outcomes

Through this project, practical experience was gained in:

- Python Programming
- Computer Vision
- Image Processing
- OpenCV
- Deep Learning
- Convolutional Neural Networks
- Transfer Learning
- ResNet18
- PyTorch
- Torchvision
- Data Augmentation
- Model Training
- Model Evaluation
- Confusion Matrix
- Precision, Recall and F1-Score
- Tkinter GUI Development

## Course Connection

This project was developed using concepts learned from:

Complete Computer Vision Bootcamp With PyTorch & TensorFlow

The course covered topics including:

- Python
- Deep Learning
- Artificial Neural Networks
- CNN
- Computer Vision
- OpenCV
- PyTorch
- Image Classification
- Data Augmentation
- Object Detection
- Image Segmentation
- Transfer Learning

The concepts learned from the course were applied to develop this Fake Image Detection system.

## Author

Agam Juneja
B.Tech CSE Core
Sikkim Manipal Institute of Technology

## Disclaimer

This project is developed for educational and academic purposes.

The predictions generated by the model represent the model's learned classification based on its training data. They should not be considered definitive proof that an image is authentic or manipulated.

## Acknowledgement

This project uses open-source technologies and resources including PyTorch, Torchvision, OpenCV, Scikit-learn, Matplotlib, Seaborn, Pillow, and the CASIA 2.0 Image Tampering Detection Dataset.