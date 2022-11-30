# A program that detects the hand landmarks

import cv2
import mediapipe as mp
from hand_utils import *

# Load the detector
mpHands = mp.solutions.hands

# Load mpDraw
mpDraw = mp.solutions.drawing_utils

# Load the predictor
hands = mpHands.Hands()

# Read the image
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Generate rgb image
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Use detector to find landmarks
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
            # Draw numbers on the landmarks
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
                isThumbOpen = is_thumbs_open(cv2, frame, w, h, hand_landmarks)
                isIndexUp = is_finger_up(cv2, frame, w, h, hand_landmarks, 5)
                isMiddleUp = is_finger_up(cv2, frame, w, h, hand_landmarks, 9)
                isRingUp = is_finger_up(cv2, frame, w, h, hand_landmarks, 13)
                isPinkyUp = is_finger_up(cv2, frame, w, h, hand_landmarks, 17)
                isPinching = is_pinching(cv2, frame, w, h, hand_landmarks)
                fingers = 0
                if isThumbOpen:
                    fingers += 1
                if isIndexUp:
                    fingers += 1
                if isMiddleUp:
                    fingers += 1
                if isRingUp:
                    fingers += 1
                if isPinkyUp:
                    fingers += 1

                cv2.putText(frame, str(fingers),
                            (int(hand_landmarks.landmark[4].x * w) + 15, int(hand_landmarks.landmark[4].y * h) - 50),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)



    # Show the image
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()