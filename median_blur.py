import cv2

image = cv2.imread(r"G:\opencv\open-cv-images\flower.jpg")

if image is None:
    print("no image")

else:
    med = cv2.medianBlur(image, 21)
    cv2.imshow("og image",image)
    cv2.imshow("med image",med)
    cv2.waitKey(0)
    cv2.destroyAllWindows()