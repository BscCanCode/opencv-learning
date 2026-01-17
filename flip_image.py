import cv2

image = cv2.imread("scene.jpg")

if image is not None:
    user_input = input("Image should be flipped: Verticall or Horizontally or both? Vertical/Horizontal/both: ").lower()
    if user_input == "vertical":
        vert_image = cv2.flip(image,0)
        cv2.imshow("Vertical image",vert_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save = input("would you like to save the image? yes/no: ").lower()
        if save == "yes":
            file_name = input("Give your file a name but note keep the extension same as original image!: ")
            cv2.imwrite(file_name,vert_image)
            print(f"Your {file_name} image is saved successfully!")
        elif save == "no":
            print("Image only viewed and not saved!")
        else:
            print("Enter proper input yes/no, no other input other than yes or no are accepted and try again with proper input!")

    elif user_input == "horizontal":
        horz_image = cv2.flip(image,1)
        cv2.imshow("horizontal_image",horz_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        user = input("Would you like to save the image?: yes/no: ").lower()

        if user == "yes":
            filename = input("Enter the file_name and note keep the extension of file same as original image: ")
            cv2.imwrite(filename,horz_image)
            print(f"Your {filename} image is saved successfully!")
        
        elif user == "no":
            print("Image is only viewed and not saved!")
        
        else:
            print("Enter proper input yes/no, no other input other than yes or no are accepted and try again with proper input!")

    elif user_input == "both":
        both = cv2.flip(image, -1)
        cv2.imshow("Horizontal and vertically flipped image",both)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        users = input("Would you like to save the image? yes/no: ").lower()
        if users == "yes":
            files_name = input("Enter the file name but note keep the extension of file same as original image: ")
            cv2.imwrite(files_name,both)
            print("File saved successfully!")
        elif users == "no":
            print("File only viewed and not saved!")
        else:
            print("Enter proper input yes/no, no other input other than yes or no are accepted and try again with proper input!")

    else:
        print("Enter the proper input vertical/horizaontal/both, and please try again!")
else:
    print("Image is not loaded properly, ensure image is loaded properly and try again!")             