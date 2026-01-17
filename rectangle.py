import cv2

image = cv2.imread("scene.jpg")

if image is not None:
    ptr1 = (50,50)
    ptr2 = (200,150)
    color = (0,0,0)
    thickness = 5

    image_copy = image.copy()
    rect = cv2.rectangle(image_copy,ptr1,ptr2,color,thickness)

    cv2.imshow("original_image",image)
    cv2.imshow("rectangle_image",rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded")