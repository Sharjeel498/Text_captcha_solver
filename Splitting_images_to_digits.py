import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
counter = 0

if getattr(sys, 'frozen', False):
    # Running as compiled .exe
    base_path = os.path.dirname(sys.executable)
else:
    # Running as script
    base_path = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(base_path, "captcha_images")
for i, file in enumerate(os.listdir(data_dir)):
    image = cv2.imread(os.path.join(data_dir, file))
    red_channel = image[:, :, 2]
    ret, clean_image = cv2.threshold(red_channel, 80, 255, cv2.THRESH_BINARY_INV)
    contours, heirarchy = cv2.findContours(clean_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    preprocessed_digits = []
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        
        # Creating a rectangle around the digit in the original image (for displaying the digits fetched via contours)
        #adding or subtracting pixels to get the complete digit in the rectangle
        cv2.rectangle(clean_image, (x - 3,y - 3), (x+w+ 2, y+h + 2), color=(0, 255, 0), thickness=2)
        
        digit = clean_image[y:y+h, x:x+w]
        
        # Resizing that digit to (18, 18)
        resized_digit = cv2.resize(digit, (18,18))
        
        # Padding the digit with 5 pixels of black color
        padded_digit = np.pad(resized_digit, ((5,5),(5,5)), "constant", constant_values=0)
        preprocessed_digits.append(padded_digit)
    
    for j, digit in enumerate(preprocessed_digits):
        cv2.imwrite(os.path.join((os.path.join(base_path, "Single_digit_samples")), f"{file[j]}_{counter}.jpg"), digit)
        counter += 1
        print(f"i is {i}")
        print(f"j is {j}")
    

    