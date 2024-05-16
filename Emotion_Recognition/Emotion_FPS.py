from ultralytics import YOLO
import cv2
import math
import time
import pygame

pygame.init()
pygame.mixer.init()

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model = YOLO("E:/Webcam_DMS/Emotion_Recognition/best.pt")
classNames = ["Nervous", "Normal"]

# Load audio file
audio_file = "E:/Webcam_DMS/Emotion_Recognition/beep.mp3"  # Adjust the path to your audio file
pygame.mixer.music.load(audio_file)
while True:
    start_time = time.time()  # Record start time before processing each frame
    success, img = cap.read()
    results = model(img, stream=True)
    # Initialize dictionaries to store confidence levels for each class
    confidences_normal = {}
    confidences_nervous = {}
    # Loop through results to process bounding boxes
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            class_name = classNames[cls]
            label = f'{class_name}{conf}'

            # Store confidence level for each class
            if class_name == "Normal":
                confidences_normal[(x1, y1)] = conf
            elif class_name == "Nervous":
                confidences_nervous[(x1, y1)] = conf

            t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
            c2 = x1 + t_size[0], y1 - t_size[1] - 3
            cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
            cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

    # Display confidence levels separately in the camera feed
    for (x, y), confidence in confidences_normal.items():
        cv2.putText(img, f'Normal %: {confidence * 100:.2f}%', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    for (x, y), confidence in confidences_nervous.items():
        cv2.putText(img, f'Nervous %: {confidence * 100:.2f}%', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display "ANTI-THEFT DETECTION!" message if "Nervous" class is detected
    if confidences_nervous:
        cv2.putText(img, "ANTI-THEFT DETECTION!", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # Play the audio
        if not pygame.mixer.music.get_busy():  # Check if the audio is not already playing
            pygame.mixer.music.play()

    out.write(img)
    cv2.imshow("Image", img)

    end_time = time.time()  # Record end time after processing each frame
    total_time = end_time - start_time  # Calculate total time taken to process each frame
    fps = 1 / total_time  # Calculate frames per second (FPS)
    print(f"FPS: {fps}")  # Print FPS

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
pygame.mixer.quit()  # Stop the mixer when the loop ends