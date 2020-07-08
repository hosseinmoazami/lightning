import cv2 as cv
import numpy as np

img = cv.imread("./lightning.jpg")

lower = (190, 180, 180)
upper = (255, 255, 255)
mask = cv.inRange(img, lower, upper)
img[mask != 0] = [0, 0, 255]

cv.imwrite("result.jpg", img)
cv.imshow("my image", img)
cv.waitKey(0)
