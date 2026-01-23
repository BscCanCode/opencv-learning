import cv2

image = cv2.imread("G:\opencv\open-cv-images\shapess.png")

image_copy = cv2.imread("G:\opencv\open-cv-images\shapess.png",cv2.IMREAD_GRAYSCALE)
_,binary = cv2.threshold(image_copy, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(binary, contours, -1, (20,255,25), 5)
cv2.imshow("og_image",image)
cv2.imshow("image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()