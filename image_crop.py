import cv2

image = cv2.imread("G:\opencv\ROC_Curve.png")

if image is not None:
    cropped = image[50:300,300:800]
    cv2.imshow("original image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Shape of original image: ",image.shape)

    cv2.imshow("Cropped_Image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Shape of cropped image is: ", cropped.shape)

else:
    print("Image is not loaded properly")

