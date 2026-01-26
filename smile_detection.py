import cv2

face_cascade = cv2.CascadeClassifier(r"open-cv-images\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"G:\opencv\open-cv-images\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video not playing, try again!")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.05, 5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]

        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smile)>0:
            cv2.putText(frame, "Smile_detected", (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1)

    cv2.imshow("Smile_detection", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quit")
        break
cap.release()
cv2.destroyAllWindows()