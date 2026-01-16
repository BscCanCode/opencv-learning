import cv2

user_input = input("Enter the location of image: ")
image = cv2.imread(user_input)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decision = input("Would you like to view or save the image or both? save/view/both:\n")

    if decision == "view":
        cv2.imshow("gray image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif decision == "save":
        filename = input("Give your file name (also include extension of the file and ke2ep it same as input file): ")
        cv2.imwrite(filename,gray)

    elif decision == "both":
        cv2.imshow("gray_image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        filename = input("Give your file name (also include extension of the file and keep it same as input file): ")
        cv2.imwrite(filename,gray)

    else:
        print("Enter the proper decision and try again")
        
else:
    print("Image is not loaded properly, check the image path and try again!")