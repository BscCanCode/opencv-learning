import cv2
image = cv2.imread(r"G:\opencv\open-cv-images\scene.jpg")

if image is  None:
    print("Image not loaded!")
    exit()
blurred_image = cv2.GaussianBlur(image, (3,3), 5)

cv2.imshow("Og image",image)
cv2.imshow("blur_image",blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
