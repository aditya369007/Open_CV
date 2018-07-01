import cv2
import numpy as np

# creating an image of a line
image = np.zeros((512, 512, 3), np.uint8)
cv2.line(image, (0, 0), (511, 511), (255, 255, 0), 5)
cv2.imshow("line", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

