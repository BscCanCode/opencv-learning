import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Video not captured!")
        break

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) == ord('q'):
        print("quit")
        break

cap.release()
cv2.destroyAllWindows()