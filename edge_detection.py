import cv2

image = cv2.imread("G:\opencv\open-cv-images\scene.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:
    edge = cv2.Canny(image, 50, 150)
    cv2.imshow("Og_image", image)
    cv2.imshow("Edge_detected_image", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not loaded properly!")