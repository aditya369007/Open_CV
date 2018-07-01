import cv2
import numpy as np

img = cv2.imread('opencv_inv.png')

cv2.imshow('Original', img)
cv2.waitKey(0)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('erosion', erosion)
cv2.waitKey(0)

dialation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('dialation', dialation)
cv2.waitKey(0)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.waitKey(0)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.waitKey(0)

