import cv2

image = cv2.imread(r"G:\opencv\open-cv-images\sqaure.png")
output = image.copy()
gray = cv2.imread(r"G:\opencv\open-cv-images\sqaure.png", cv2.IMREAD_GRAYSCALE)

_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(output, contours, -1, (0,255,255), 5)

for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    corners = len(contour)

    if corners ==3:
        shape = "Triangle"
    elif corners ==4:
        shape = "Square"
    elif corners == 5:
        shape = "Penatgon"
    elif corners > 5:
        shape = "Circle"
    else:
        shape = "Unknown"

    cv2.drawContours(output, [approx], -1, (255,0,255), 4)

    x = approx.ravel()[0]
    y = approx.ravel()[1] -10
    cv2.putText(output, shape, (x,y), cv2.FONT_HERSHEY_DUPLEX, 3, (255,0,255), 1)

cv2.imshow("Og_image", image)
cv2.imshow("output", output)
cv2.imshow("Gray_image", gray)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()