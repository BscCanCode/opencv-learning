import cv2

image = cv2.imread(r"G:\opencv\open-cv-images\triangle.PNG")
gray = cv2.imread(r"G:\opencv\open-cv-images\triangle.PNG", cv2.IMREAD_GRAYSCALE)

_, thresh = cv2.threshold(gray, 222, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = image.copy()
cv2.drawContours(output, contours, -1, (255,0,255), 5)

cv2.imshow("Image", image)
cv2.imshow("Thresh", thresh)
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()