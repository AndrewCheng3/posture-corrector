import time
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise SystemExit("Could not open webcam")

prev = time.time()
smooth_fps = 0.0
while True:
    worked, frame = cap.read()
    if not worked:
        break

    curr = time.time()
    fps = 1/(curr - prev)
    prev = curr

    smooth_fps = fps if smooth_fps == 0 else 0.9* smooth_fps + 0.1*fps

    cv2.putText(frame, f"{smooth_fps:.0f} FPS", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Webcam", frame)

    if (cv2.waitKey(1) & 0xFF) == ord("q"): #evaluates last 8 binary values
        break

cap.release()
cv2.destroyAllWindows()

