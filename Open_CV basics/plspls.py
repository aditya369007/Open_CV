import cv2
import numpy as np

input_1 = cv2.imread('input.jpg')
cv2.imshow('Test', input_1)
print (input_1.shape)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('op.jpg', input_1)

