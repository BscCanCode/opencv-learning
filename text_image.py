import cv2

image = cv2.imread("scene.jpg")

if image is not None:
    image_copy = image.copy()
    text = cv2.putText(image_copy,"This is just a beautiful scenery",(20,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)

    cv2.imshow("Original_image",image)
    cv2.imshow("Texted_image",text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded properly")
