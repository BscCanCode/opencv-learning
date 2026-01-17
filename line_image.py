import cv2

image = cv2.imread("scene.jpg")

if image is not None:
    ptr1 = (50,50)
    ptr2 = (400,400)
    color = (255,0,255)
    thickness = 5
    image_copy = image.copy()
    lined_image = cv2.line(image_copy,ptr1, ptr2, color, thickness)

    cv2.imshow("Original image",image)
    cv2.imshow("line_on_image",lined_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded, try again!")