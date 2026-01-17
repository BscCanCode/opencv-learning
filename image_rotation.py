import cv2

image = cv2.imread("scene.jpg")

if image is None:
    print("Image is not loaded successfully")
else:
    h,w = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center,50,1)
    rotated = cv2.warpAffine(image,M,(150,150))

    cv2.imshow("original_image",image)
    cv2.imshow("Rotated_image",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
