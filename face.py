# A program that detects the facial points

import cv2
import dlib

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
# Download from https://github.com/severin-lemaignan/gazr/raw/master/share/shape_predictor_68_face_landmarks.dat
predictor = dlib.shape_predictor("predictors/shape_predictor_68_face_landmarks.dat")

# Read the image
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use detector to find landmarks
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # Create landmark object
        landmarks = predictor(gray, face)

        # Loop through all the points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

        # Draw an arrow next to the face indicating the direction of the eye movement
        # Get the left and right eye coordinates
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)

    # Flip image
    frame = cv2.flip(frame, 1)

    # Show the image
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
