import cv2

image = cv2.imread("G:\opencv\ROC_Curve.png")

if image is not None:
    resize = cv2.resize(image,(500,500))

    print("Shape of Original image:",image.shape)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Shape of resized image is: ",resize.shape)
    cv2.imshow("resized",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded, try again")
