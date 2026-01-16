import cv2

image = cv2.imread("G:\\opencv\\ROC_Curve.png")
if image is None:
    print("Error loading image")
else:
    cv2.imshow("ROC CURVE",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
