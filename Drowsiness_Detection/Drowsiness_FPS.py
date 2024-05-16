from ultralytics import YOLO
import cv2
import math
import pygame
import time

pygame.init()

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('Drowsiness_FPS_1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model = YOLO("E:/Webcam_DMS/Drowsiness/best.pt")
classNames = ["Focused", "Sleepy"]

# Load audio file
audio_file = "E:/Webcam_DMS/Drowsiness/beep.mp3"  # Change this to the path of your audio file
pygame.mixer.music.load(audio_file)

while True:
    start_time = time.time()  # Record qqstart time before processing each frame
    success, img = cap.read()
    results = model(img, stream=True)

    sleepy_detected = False

    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = box.conf[0]
            if conf >= 0.7:
                cls = int(box.cls[0])
                class_name = classNames[cls]
                if class_name == "Sleepy":
                    sleepy_detected = True

                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                conf = math.ceil((conf * 100)) / 100
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

    if sleepy_detected:
        cv2.putText(img, "BE CONSCIOUS WHILE DRIVING!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                    cv2.LINE_AA)
        # Display the confidence level in the camera feed
        cv2.putText(img, f"Drowsiness %: {conf * 100:.2f}%", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_AA)
        # Play the audio
        if not pygame.mixer.music.get_busy():  # Check if the audio is not already playing
            pygame.mixer.music.play()

    else:
        # Stop the audio if "Sleepy" class is not detected
        pygame.mixer.music.stop()

    out.write(img)
    cv2.imshow("Image", img)

    end_time = time.time()  # Record end time after processing each frame
    total_time = end_time - start_time  # Calculate total time taken to process each frame
    fps = 1 / total_time  # Calculate frames per second (FPS)
    print(f"FPS: {fps}")  # Print FPS

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
