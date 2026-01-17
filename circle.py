import cv2

image = cv2.imread("scene.jpg")

if image is not None:
    image_copy = image.copy()
    center = (140,105)
    radius = 50
    color = (255,255,0)
    thickness = 5
    circle = cv2.circle(image_copy, center, radius, color, thickness)

    cv2.imshow("Original_image", image)
    cv2.imshow("Circle_image",circle)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded, try again!")