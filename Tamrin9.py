import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

degree = 0

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        fingerCount = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                handLandmarks = []

                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y, landmarks.z])

                AB = (handLandmarks[8][0] - handLandmarks[5][0], handLandmarks[8][1] - handLandmarks[5][1], handLandmarks[8][2] - handLandmarks[5][2])
                AC = (handLandmarks[4][0] - handLandmarks[5][0], handLandmarks[4][1] - handLandmarks[5][1], handLandmarks[4][2] - handLandmarks[5][2])
                dot_product = sum(AB[i] * AC[i] for i in range(3))
                magnitude_AB = math.sqrt(sum(AB[i] ** 2 for i in range(3)))
                magnitude_AC = math.sqrt(sum(AC[i] ** 2 for i in range(3)))
                angle_radians = math.acos(dot_product / (magnitude_AB * magnitude_AC))
                angle_degrees = math.degrees(angle_radians)
                print("Angle between the vectors:", angle_degrees, "degrees")

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        cv2.putText(image, str(degree), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)

        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the webcam:
cap.release()
