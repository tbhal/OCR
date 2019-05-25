

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import time
import numpy as np

start_time = time.clock()


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")

args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshed_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)
# find contours and get the external one
(img, contours, hier) = cv2.findContours(threshed_img, cv2.RETR_TREE,
                cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow("Image", gray)

# check to see if we should apply thresholding to preprocess the
# image
#if args["preprocess"] == "thresh":
#    gray = cv2.threshold(gray, 0, 255,
#                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
#elif args["preprocess"] == "blur":
#    gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
#print("--- {} seconds ---".format(time.time() - start_time))
print((time.clock() - start_time))


for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)



# show the output images
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", image)
cv2.waitKey(0)
ESC = 27
while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
