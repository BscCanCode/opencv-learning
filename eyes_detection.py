import cv2

face_cascade = cv2.CascadeClassifier(r"G:\opencv\open-cv-images\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"G:\opencv\open-cv-images\haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video not playing, try again!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]


        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes)>0:
            cv2.putText(frame, "eyes detected", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255), 2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quit")
        break

    cv2.imshow("eye_detector", frame)

cap.release()
cv2.destroyAllWindows()    
