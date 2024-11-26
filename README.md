## Text_captcha_solver
This project demonstrates the creation of an Image recognition model for recognizing single-digit numbers from CAPTCHA images. Using TensorFlow/Keras, a Convolutional Neural Network (CNN) is trained and converted to TensorFlow Lite for efficient deployment. The solution includes data preprocessing, contour detection, and digit classification.

## Features
- **Preprocessing pipeline**:
  - Converts images to grayscale and normalizes pixel values.
  - Isolates digits from noisy CAPTCHA images using contour detection.
- **CNN architecture** for digit recognition.
- **TensorFlow Lite model** for lightweight and fast inference.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sharjeel498/Text_captcha_solver.git

## Usage

  Train the Model:
  Run train_model.py to train the model and save it as model.tflite.
  
  Predict CAPTCHA:

  ```python
  from predict import pred_captcha
  predicted_text = pred_captcha("path/to/captcha/image.png", 28, 28, 1)
  print(f"Predicted CAPTCHA: {predicted_text}")
  ```
## Results
Loss: 0.16707107424736023 <br>
Accuracy: 0.9922480583190918 <br>
Precision: 0.9937888383865356 <br>
Recall: 0.9922480583190918 <br>
