import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive
import os

# mount google drive to access input image and save output images
drive.mount('/content/drive')

# set input image path
input_image_path = '/content/drive/My Drive/input_image.jpg'

# read input image
img = cv2.imread(input_image_path)

# convert image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create output directory if it does not exist
output_dir = '/content/drive/My Drive/output_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# generate different hue images
for hue in range(0, 180, 5):
    # set hue value
    hsv_img[:, :, 0] = hue
    # convert image back to BGR color space
    bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    # set output image path
    output_image_path = os.path.join(output_dir, f'hue_{hue}.jpg')
    # save image to output directory
    cv2.imwrite(output_image_path, bgr_img)

# display message after processing all images
print('Images saved successfully!')

# close window
cv2.destroyAllWindows()
