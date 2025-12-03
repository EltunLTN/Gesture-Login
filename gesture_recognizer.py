import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def fingers_up(hand_landmarks):
    """
    MediaPipe landmarks-ə əsasən hansı barmaqların açıq olduğunu qaytarır.
    Return: [Thumb, Index, Middle, Ring, Pinky], hər biri 1 (açıq) və ya 0 (bağlı)
    """
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Digər barmaqlar üçün
    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

def recognize_gesture():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)  # Mirror image
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            gesture = None

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = fingers_up(hand_landmarks)

                # V-sign: index və middle açıq, digərləri bağlı
                if fingers == [0,1,1,0,0]:
                    gesture = "V-sign"
                # Əlavə jestlər üçün buraya əlavə edə bilərsən, məsələn:
                elif fingers == [0,1,0,0,0]:
                    gesture = "One"
                elif fingers == [0,1,1,1,1]:
                    gesture = "Four"
                elif fingers == [1,1,1,1,1]:
                    gesture = "Five"

                if gesture:
                    cv2.putText(frame, f"Gesture: {gesture}", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.imshow("Gesture Recognition", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == 27 or gesture is not None:
                break

    cap.release()
    cv2.destroyAllWindows()
    return gesture
