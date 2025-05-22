import cv2

# Create a named window
cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)

# Set the desired position (x, y)
x_pos = 1000  # x position
y_pos = 100  # y position
cv2.moveWindow('Camera Feed', x_pos, y_pos)

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show the frame in the named window
    cv2.imshow('Camera Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
