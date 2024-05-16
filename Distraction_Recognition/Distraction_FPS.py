from ultralytics import YOLO
import cv2
import math
import time

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model = YOLO("E:/Webcam_DMS/Distraction/best.pt")
classNames = ["Drinking", "Mobile"]

while True:
    start_time = time.time()  # Record start time before processing each frame

    success, img = cap.read()
    results = model(img, stream=True)
    distracted = False  # Flag to indicate if driver is distracted
    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = box.conf[0]
            if conf >= 0.7:  # Limiting confidence level
                cls = int(box.cls[0])
                class_name = classNames[cls]
                if class_name in ["Mobile", "Drinking"]:
                    distracted = True
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    conf = math.ceil((conf * 100)) / 100
                    label = f'{class_name} {conf}'
                    t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                    c2 = x1 + t_size[0], y1 - t_size[1] - 3
                    cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
    if distracted:
        cv2.putText(img, "DRIVER DISTRACTED!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display confidence level separately in the camera feed
    if distracted:
        cv2.putText(img, f"Distracted %: {conf * 100:.2f}%", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_AA)

    out.write(img)
    cv2.imshow("Image", img)

    end_time = time.time()  # Record end time after processing each frame
    total_time = end_time - start_time  # Calculate total time taken to process each frame
    fps = 1 / total_time  # Calculate frames per second (FPS)
    print(f"FPS: {fps}")  # Print FPS

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cv2.destroyAllWindows()
