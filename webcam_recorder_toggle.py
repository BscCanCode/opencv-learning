import cv2
print("Press r to start the recording, s to save it and q to quit!")
cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')

recorder = cv2.VideoWriter("file.mp4",codec, 30, (frame_width, frame_height))

recording = False

while True:
    ret, frame = cam.read()

    if not ret:
        print("Unsupported video format!")
        break

    if recording:
        recorder.write(frame)

    cv2.imshow("Live Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        recording = True
        print("Recording started!")
    
    elif key == ord('s'):
        recording = False
        print("Recording Saved!")

    elif key == ord('q'):
        print("Quit")
        break 

cam.release()
recorder.release()
cv2.destroyAllWindows()