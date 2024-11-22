import cv2
import os
import numpy as np
import sys


if getattr(sys, 'frozen', False):
    # Running as compiled .exe
    base_path = os.path.dirname(sys.executable)
else:
    # Running as script
    base_path = os.path.dirname(os.path.abspath(__file__))
sample_dir = os.listdir("E:\\Development\\bot_python\\bright_data_bot\\captcha_images")
for i, file in enumerate(sample_dir):
    image = cv2.imread(os.path.join("E:\\Development\\bot_python\\bright_data_bot\\captcha_images",file))
    red_channel = image[:, :, 2]
    ret, clean_image = cv2.threshold(red_channel, 80, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(os.path.join("E:\\Development\\bot_python\\bright_data_bot\\processed_captcha_80_INV", file), clean_image)