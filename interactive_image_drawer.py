import cv2
import sys

user = input("Enter the path of your image: ")
image = cv2.imread(user)

if image is not None:
    option = input("Which shape would you like to draw on your image?\n1.Circle\n2.Rectangle\n3.Text_on_image\n4.line_on_image\n5.Exit\nYour input: ").lower()
    image_copy = image.copy()
    if option == "circle":
        center = input("Enter x,y co-ordinates: ")
        x,y = map(int,center.split(","))
        center = (x,y)
        radius = int(input("Enter in integer how huge the circle should be: "))
        color = input("Enter the color you want to give your circle in scalar form ex. 255,0,0: ")
        x,y,z = map(int,color.split(","))
        color = (x,y,z)
        thickness = int(input("Enter how thick the borderline of circle should be in integer: "))
        cv2.circle(image_copy,center,radius,color,thickness)
        cv2.imshow("Original_image",image)
        cv2.imshow("circle_image",image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save = input("Would you like to save this image? yes/no: ").lower()
        if save == "yes":
            file_name = input("Enter you file name keep the extension same as input image:")
            cv2.imwrite(file_name,image_copy)
            print(f" Your image {file_name} is saved successfully!")
        elif save == "no":
            print("Image is only viewed not saved!")       
        else:
            print("Enter the proper input yes/no and try again!")

    elif option == "rectangle":
        pt1 = input("Enter the co-ordinates in x,y:  ")
        x,y = map(int,pt1.split(","))
        pt1 = (x,y)
        pt2 = input("Enter the another co-ordinates in x,y format: ")
        x1,y1 = map(int,pt2.split(","))
        pt2 = (x1,y1)
        color = input("Enter the color in the form of scalar ex. 255,0,0: ")
        x2,y2,z2 = map(int,color.split(","))
        color = (x2,y2,z2)
        thick = int(input("Enter the thickness of your rectangle: "))
        cv2.rectangle(image_copy,pt1,pt2,color,thick)
        cv2.imshow("Original_image",image)
        cv2.imshow("rectangle_image",image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        saves = input("Would you like to save the rectangle image? yes/no: ").lower()
        if saves == "yes":
            name = input("Give name to your file but keep the extension same as image given as input: ")
            cv2.imwrite(name,image_copy)
            print(f"Your image {name} is saved successfully!")
        elif saves == "no":
            print("You only viewed the image and its not saved!")
        else:
            print("Enter the proper input yes/no, try again!")
    
    elif option == "line_on_image":
        pt1 = input("Enter the co-ordinates for x,y: ")
        x,y = map(int,pt1.split(","))
        pt1 = (x,y)
        pt2 = input("Enter the co-ordinates for x2 and y2: ")
        x2,y2 = map(int,pt2.split(","))
        pt2 = (x2,y2)
        color = input("enter the color in scalar format ex. 255,255,0: ")
        x,y,z = map(int,color.split(","))
        color = (x,y,z)
        thickness = int(input("Enter the thickness of the line: "))
        cv2.line(image_copy,pt1,pt2,color,thickness)
        cv2.imshow("Original_image",image)
        cv2.imshow("Line_image",image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save = input("Would you like to save the image? yes/no: ").lower()
        if save == "yes":
            file_name = input("Give the name to your file: ")
            cv2.imwrite(file_name,image_copy)
            print(f"Your image {file_name} is saved successfully!")
        elif save == "no":
            print("Image only viewed and not saved!")
        else:
            print("Enter the proper input yes/no, and try again!")

    elif option == "text_on_image":
        text = input("Enter the text to write on image: ")
        org = input("Enter the co-ordinates of x,y: ")
        x,y = map(int,org.split(","))
        org = (x,y)
        font = cv2.FONT_HERSHEY_DUPLEX
        size = float(input("Enter the size of the text: "))
        color = input("Enter the color in scalar form ex=255,255,255: ")
        x,y,z = map(int,color.split(","))
        color = (x,y,z)
        thick = int(input("Enter the thickness of the text: "))
        cv2.putText(image_copy,text,org,font,size,color,thick)

        cv2.imshow("original_image",image)
        cv2.imshow("text_image",image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        save = input("Would you like to save the image? yes/no: ").lower()
        if save == "yes":
            file_name = input("Enter the name of your file, put the extension same as input image: ")
            cv2.imwrite(file_name,image_copy)
            print(f"Your image {file_name} is saved successfully!")
        elif save == "no":
            print("Image is viwed but not saved!")
        else:
            print("Enter the proper input yes/no and try again!")
    
    elif option == "exit":
        print("You have exited successfully!")
        sys.exit()
    
    else:
        print("Enter the proper input, check the options and try again!")

else:
    print("Image is not loaded, maybe the file path is incorrect, check the path and try again!")