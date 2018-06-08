# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 01:48:59 2018

@author: tushar
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
src_path = "/home/tushar/Documents/testOCR/"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread('/home/tushar/Documents/testOCR/example_03.png')

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result


print('--- Start recognize text from image ---')
print(get_string(src_path + "Epo Automation Content.jpeg"))

print("------ Done -------")
