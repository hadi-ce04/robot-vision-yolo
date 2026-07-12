import cv2
from ultralytics import YOLO

def main():
    # Load a pre-trained YOLOv8 nano model (lightweight, perfect for real-time robot vision)
    model = YOLO("yolov8m.pt")

    # Initialize webcam (0 is usually the default built-in camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Robot Vision Active. Press 'q' to quit.")

    while True:
        # Capture frame-by-frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Run YOLO inference on the frame
        # stream=True utilizes generator syntax for better memory efficiency
        results = model(frame, stream=True)

        # Visualize the results on the frame
        for result in results:
            annotated_frame = result.plot()

        # Display the resulting frame in a window
        cv2.imshow("Robot Vision - YOLO", annotated_frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up and close windows when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()