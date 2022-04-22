# importing the modules
import cv2
import numpy as np
# Reading the image
image = cv2.imread('C:\\Users\\Dell India\\PycharmProjects\\pythonProject\\image - Copy.jpg')
#BY SARTHAK VASHISHTHA
# Creating the kernel(2d convolution matrix)
kernel = np.array([[1, 1, 1],
					[1, -8, 1],
					[1, 1, 1]])

# Applying the filter function
img = cv2.filter2D(src=image, ddepth=-4, kernel=kernel)

# Showing the original and output image
cv2.imshow('Original', image)
cv2.imshow('Contaminated', img)
cv2.waitKey()