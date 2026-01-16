import cv2

image = cv2.imread("G:\opencv\ROC_Curve.png")

if image is not None:
    h, w, c = image.shape
    print(f"The loaded image has following attributes: \nHeight:{h}\nWidth:{w}\nChannels:{c}")
    
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded")

