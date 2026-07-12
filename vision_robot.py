import cv2
from ultralytics import YOLO

def main():
    model = YOLO("yolov8m.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Robot Vision Active. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        results = model(frame, stream=True)

        for result in results:
            annotated_frame = result.plot()

        cv2.imshow("Robot Vision - YOLO", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
