import cv2
import numpy as np

inp = cv2.imread('input.jpg')

height, width = inp.shape[:2]

print(height, width)

quarter_height, quarter_width = height/4, width/4

# Translation Matrix formation

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

img_translate = cv2.warpAffine(inp, T, (width, height))
cv2.imshow('Translation', img_translate)
cv2.waitKey()
cv2.destroyAllWindows()
