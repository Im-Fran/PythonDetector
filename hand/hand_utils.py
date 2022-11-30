def is_finger_up(cv2, frame, w, h, hand_landmarks, landmark_id):
    x1, y1 = hand_landmarks.landmark[landmark_id+3].x, hand_landmarks.landmark[landmark_id+3].y
    x2, y2 = hand_landmarks.landmark[landmark_id].x, hand_landmarks.landmark[landmark_id].y
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if length > ((hand_landmarks.landmark[landmark_id+2].x - x1) ** 2 + (hand_landmarks.landmark[landmark_id+2].y - y1) ** 2) ** 0.5:
        if y1 < hand_landmarks.landmark[landmark_id].y and y1 < hand_landmarks.landmark[landmark_id+1].y and y1 < hand_landmarks.landmark[landmark_id+2].y:
            cv2.putText(frame, "Finger up", (int(x1 * w)+12, int(y1 * h)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
            return True
    return False

def is_thumbs_open(cv2, frame, w, h, hand_landmarks):
    # Get distance between landmark 4 and 3
    distance = ((hand_landmarks.landmark[4].x - hand_landmarks.landmark[3].x) ** 2 + (hand_landmarks.landmark[4].y - hand_landmarks.landmark[3].y) ** 2) ** 0.5
    # Now get distance between landmark 4 and 5
    distance2 = ((hand_landmarks.landmark[4].x - hand_landmarks.landmark[5].x) ** 2 + (hand_landmarks.landmark[4].y - hand_landmarks.landmark[5].y) ** 2) ** 0.5
    if distance2 > (distance*1.5):
        cv2.putText(frame, "Thumbs open", (int(hand_landmarks.landmark[4].x * w)+12, int(hand_landmarks.landmark[4].y * h)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
        return True
    return False

def is_pinching(cv2, frame, w, h, hand_landmarks):
    # Detect if the index finger and the thumb are touching
    distance = ((hand_landmarks.landmark[4].x - hand_landmarks.landmark[8].x) ** 2 + (hand_landmarks.landmark[4].y - hand_landmarks.landmark[8].y) ** 2) ** 0.5
    if distance < 0.05:
        cv2.putText(frame, "Pinching", (int(hand_landmarks.landmark[4].x * w)+15, int(hand_landmarks.landmark[4].y * h)-70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
        return True
    return False
