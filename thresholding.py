import cv2

image = cv2.imread("G:\opencv\open-cv-images\scene.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:
    ret, thresh_image = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow("original_image", image)
    cv2.imshow("thresh_image", thresh_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded properly!")