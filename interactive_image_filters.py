import cv2
import numpy as np

user =  input("Enter the path of your image: ")
image = cv2.imread(user)


if image is None:
    print("Image is not loaded properly, try again!")
else:
    image_copy = image.copy()
    print("Various image blurring techinques!")
    while True:
        user_input = input("Enter your prefered technique. Gaussian/Median/Sharpened/Exit?").lower()
        if user_input == "gaussian":
            blur = input("Enter how much blur you want enter in ex. x, y only odd numbers are accepted and x =y is the condition!: ")
            x,y = map(int, blur.split(","))
            blur = (x,y)
            decide = int(input("Enter the degree of the blur you want in your image: "))
            image_copy = cv2.GaussianBlur(image_copy, blur, decide)
            cv2.imshow("Original_Image",image)
            cv2.imshow("Gaussian_Image", image_copy)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user_input == "median":
            kernel = int(input("Enter the size of kernel you want in your image: "))
            image_copy = cv2.medianBlur(image_copy, kernel)
            cv2.imshow("Original_image", image)
            cv2.imshow("Median_Blured_Image", image_copy)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user_input == "sharpened":
            kernel = np.array([
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ])
            image_copy = cv2.filter2D(image_copy, -1, kernel)
            cv2.imshow("Original_Image", image)
            cv2.imshow("Sharpened_Image", image_copy)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user_input == 'exit':
            print("Exit is done!")
            exit()
        else:
            print("Enter the proper input, and try again!")
