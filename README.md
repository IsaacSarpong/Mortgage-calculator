# Shift Digit Image in Python
In this project, we will be shifting a digit image up, down, left, and right using Python. We will use the OpenCV library for image processing and manipulation.

## Requirements
The following libraries are required to run this project:

OpenCV
NumPy
You can install the libraries using the following commands:

pip install opencv-python
pip install numpy

## Image Dataset
We will be using the MNIST dataset for this project. The MNIST dataset consists of handwritten digits and is widely used for image classification tasks.

To download the MNIST dataset, you can use the following command:


wget https://github.com/myleott/mnist_png/raw/master/mnist_png.tar.gz
After downloading the dataset, extract it using the following command:

tar -zxvf mnist_png.tar.gz
The extracted folder will contain two subfolders, training and testing, which contain the images for training and testing respectively.


## Image Shifting
We will define a function shift_image that takes an input image and the shift amount as parameters and returns the shifted image. The shift amount can be positive or negative, which determines the direction of the shift.

python

import cv2
import numpy as np

def shift_image(img, shift):
    rows, cols = img.shape
    M = np.float32([[1, 0, shift[0]], [0, 1, shift[1]]])
    shifted_img = cv2.warpAffine(img, M, (cols, rows))
    return shifted_img
The function shift_image takes an input image img and the shift amount as a tuple shift. It first calculates the number of rows and columns of the input image using the shape property of the NumPy array. It then defines a transformation matrix M that represents the shift using the warpAffine function of OpenCV. Finally, it applies the transformation to the input image using the warpAffine function and returns the shifted image.

We can use the shift_image function to shift an image in any direction. For example, to shift an image up by 10 pixels, we can use the following code:

python

img = cv2.imread('path/to/image.png', cv2.IMREAD_GRAYSCALE)
shifted_img = shift_image(img, (-10, 0))
Similarly, we can shift an image down, left, or right by changing the shift amount accordingly.