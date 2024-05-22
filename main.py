import os
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


numbers = [1, 2, 3, 4]
values = ["one", "two", "three", "four"]


pairs = {(number, value) for number, value in zip(numbers, values)}

dict_pairs = dict((number, value) for number, value in zip(numbers, values))


print(dict_pairs)

img = cv.imread("C:/Users/x4v33r/Downloads/image.jpg")

kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

success = cv.imwrite("C:/Users/x4v33r/Downloads/blurred.jpg", dst)

if success:
    print(f"Image {success} saved")
else:
    print("Cannot save image")


fig, axes = plt.subplots(nrows=1, ncols=2)


# Display each image in a subplot
axes[0].imshow(img)
axes[0].set_title("Image 1")

axes[1].imshow(dst)
axes[1].set_title("Image 2")

plt.show()
