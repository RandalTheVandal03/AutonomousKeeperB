import cv2

#make object for video capture
print("Possibe Cameras:")
for i in range (10):
    print(cv2.VideoCapture(i).getBackendName())
    print(cv2.VideoCapture(i).isOpened())

capture = cv2.VideoCapture(0)

#check if camera opened
if not capture.isOpened():
    print("Error camera is not working!")

while True:
    #captuer frames
    ret, frame = capture.read()

    if not ret:
        print("Cant receive frames. stream ended?... Exiting")
        break
    
    cv2.imshow('Live Feed', frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
