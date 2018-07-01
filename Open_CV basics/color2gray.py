import cv2
# load the test image
inp = cv2.imread('input.jpg')
# displaying the test image
cv2.imshow('Original', inp)
cv2.waitKey()

# using cvtcolor to convert
gray_img = cv2.cvtColor(inp, cv2.COLOR_BGR2GRAY)

# displaying the converted image

cv2.imshow('converted_gray', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()
