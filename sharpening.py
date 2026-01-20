import cv2
import numpy as np

image = cv2.imread(r"G:\opencv\open-cv-images\blur.png")

sharpened_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
if image is None:
    print("No image loaded!")

sharp = cv2.filter2D(image, -1, sharpened_kernel)
cv2.imshow("og_image", image)
cv2.imshow("unblur_image",sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()