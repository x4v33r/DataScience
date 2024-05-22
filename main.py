import os
import sys
import cv2 as cv

numbers = [1, 2, 3, 4]
values = ["one", "two", "three", "four"]


pairs = {(number, value) for number, value in zip(numbers, values)}

dict_pairs = dict((number, value) for number, value in zip(numbers, values))


print(dict_pairs)

img = cv.imread("C:/Users/x4v33r/Downloads/image.jpg")
cv.imshow("Wallpaper", img)
k = cv.waitKey(0)  # 0
