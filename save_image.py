import cv2

image = cv2.imread("G:\\opencv\\ROC_Curve.png")

if image is not None:
    cv2.imshow("ROC_CURVE",image)
    cv2.imwrite("saved_image.png",image) #image saved using cv2 in same folder
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
else:
    print("There was an error loading the image")