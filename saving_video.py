import cv2
cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

recorder = cv2.VideoWriter("video_file.mp4",codec,30,(frame_width,frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("File is not proper!")
        break

    #recorder.write(frame)
    cv2.imshow("live_screen",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quit")
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()