import cv2
import mediapipe as mp
import serial
import time
from scipy.spatial import distance
import paho.mqtt.client as mqtt

# --------------------------------------------------
# Arduino Serial Communication
# --------------------------------------------------
ser = serial.Serial('COM12', 115200, timeout=1)
time.sleep(2)

# --------------------------------------------------
# MQTT Configuration
# --------------------------------------------------
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "drowsiness/alert"

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.connect(BROKER, PORT, 60)
mqtt_client.loop_start()

# --------------------------------------------------
# MediaPipe Face Mesh
# --------------------------------------------------
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# --------------------------------------------------
# Eye Landmarks
# --------------------------------------------------
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

EAR_THRESHOLD = 0.22
DROWSY_TIME = 2

closed_start = None
last_command = ""
alert_sent = False

cap = cv2.VideoCapture(0)


def eye_aspect_ratio(eye_points):
    A = distance.euclidean(eye_points[1], eye_points[5])
    B = distance.euclidean(eye_points[2], eye_points[4])
    C = distance.euclidean(eye_points[0], eye_points[3])

    return (A + B) / (2.0 * C)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            h, w, _ = frame.shape

            left_eye = []
            right_eye = []

            for idx in LEFT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)

                left_eye.append((x, y))

                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            for idx in RIGHT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)

                right_eye.append((x, y))

                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)

            avg_ear = (left_ear + right_ear) / 2

            cv2.putText(
                frame,
                f"EAR : {avg_ear:.2f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # ---------------------------------------------
            # Eyes Closed
            # ---------------------------------------------
            if avg_ear < EAR_THRESHOLD:

                if closed_start is None:
                    closed_start = time.time()

                elapsed = time.time() - closed_start

                cv2.putText(
                    frame,
                    f"Eyes Closed : {elapsed:.1f}s",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                if elapsed >= DROWSY_TIME:

                    cv2.putText(
                        frame,
                        "DROWSINESS DETECTED",
                        (20, 130),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3
                    )

                    # Stop Motor
                    if last_command != "a":

                        ser.write(b'a')

                        print("Motor OFF")

                        last_command = "a"

                    # MQTT Alert
                    if not alert_sent:

                        mqtt_client.publish(
                            TOPIC,
                            "⚠️ DROWSINESS DETECTED! Motor Stopped."
                        )

                        print("MQTT Alert Sent")

                        alert_sent = True

            # ---------------------------------------------
            # Eyes Open
            # ---------------------------------------------
            else:

                closed_start = None

                alert_sent = False

                cv2.putText(
                    frame,
                    "Eyes Open",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                if last_command != "A":

                    ser.write(b'A')

                    print("Motor ON")

                    last_command = "A"

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --------------------------------------------------
# Cleanup
# --------------------------------------------------
cap.release()

mqtt_client.loop_stop()
mqtt_client.disconnect()

ser.close()

cv2.destroyAllWindows()
