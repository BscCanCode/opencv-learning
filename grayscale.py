import cv2

image = cv2.imread("G:\opencv\saved_image.png")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("gray_image",gray)
    success = cv2.imwrite("gray_scale.png",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if success:
        print("Gray image is saved successfully!")
    else:
        print("There was error in saving the image!")
else:
    print("image could not load")