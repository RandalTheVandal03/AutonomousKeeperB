import cv2
from picamera2 import Picamera2

# Identify the camera index (optional, modify if needed)
camera_index = 0  # Assuming the camera is at index 0

# Initialize the PiCamera2 object
picam2 = Picamera2()

# Configure the camera for preview
config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()

while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Display the frame using OpenCV
    cv2.imshow("PiCamera2 Feed", frame)

    # Check for user input to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop the camera and close windows
picam2.stop()
cv2.destroyAllWindows()