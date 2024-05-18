# SMART DRIVER MONITORING SYSTEM - AUTODRIVE
A smart driver monitoring system is crucial for enhancing road safety. By analyzing driver behavior and detecting signs of fatigue or distraction, it can mitigate accidents, save lives, 
and promote responsible driving habits for a safer transportation environment. 
Ultimately, the implementation of such systems not only reduces the risk of accidents but also fosters a more secure and efficient transportation ecosystem for all stakeholders.

![drowsydriving](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/ad67b07f-8e90-4fbc-a827-66ceb7573493)

## Problem Statement
With the rise in accidents during road trips attributed to driver fatigue, unconsciousness, or health issues, there is a pressing need to develop a Smart Driver Monitoring System. This system aims to aid drivers in preventing such accidents by providing assistance and alerts.

## Objectives
In this project, I've outlined two objectives: one focusing on the software aspect and the other on hardware.

- The software part of the objective is to develop a smart driver monitoring system with the following features:
  - Driver’s Eye Closure Detection (Focused/Sleepy)
  - Facial Expression Analysis (Normal/Nervous)
  - Dangerous Behaviour Detection (Mobile phone usage/Drinking while Driving)
  - Driver’s Head Pose Estimation
    
- The hardware part of the objective is to prevent the vehicle from accidents, when driver loses control, by overriding the CAN BUS of the vehicle, and interpreting the ECUs in the vehicle to generate signals and function accordingly to our need. (Future Work)

## Details on the Algorithm
While there are various object detection algorithms available, YOLO (You Only Look Once) has emerged as a popular choice for our smart driver monitoring system. YOLO's real-time performance and accuracy make it a powerful tool for detecting critical driver states and behaviors.
- YOLO's single-stage architecture allows for faster processing, enabling real-time detection essential for driver monitoring applications.
- YOLO's flexible design allows for customization to detect the specific objects relevant to our driver monitoring system, such as mobile phones, coffee cups, and driver facial expressions.
- Advancements in YOLO versions have led to improved accuracy, making it a reliable choice for our safety-critical application.

## YOLO: How it Works?
- YOLO uses a single CNN to predict bounding boxes and class probabilities in a single evaluation.
- The network divides the image into a grid, predicts bounding boxes and class probabilities for each grid cell.
- YOLO achieves impressive real-time object detection speeds, making it well-suited for our driver monitoring application.
  
 ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/a7c09f55-98f6-4d8c-927f-eb2c2c81bbc2)

In the software aspect of the objective, the initial focus is on achieving three key objectives: detecting driver's eye closure, analyzing facial expressions, and identifying dangerous behaviors. To accomplish this, data collection and training are conducted using YOLO, a deep learning framework. Additionally, head pose estimation is integrated using the Mediapipe library, known for its high accuracy and pre-trained models.

## MediaPipe for Head Pose Estimation
- MediaPipe is an open-source framework by Google that provides pre-built machine learning pipelines for various tasks, including pose estimation.
- It employs pre-trained models to detect facial landmarks (like eyes, nose, mouth) in an image/video frame.
- Using these landmarks, MediaPipe calculates the relative positions and orientations, estimating the head pose (e.g., tilt, rotation).

## Workflow for Software part of Smart Driver Monitoring System

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/25692939-2fbb-4fde-9f66-91989725be13)

## Workflow for Hardware part of Smart Driver Monitoring System

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/c1c58fcd-d011-42c7-a606-0d9546013e9f)

* Till "Analyzing the Behavior of CAN" step is done till now and steps after those are kept as Future Works

## Results for Software part of Smart Driver Monitoring System
- Dataset collection is a key step in the custom model training, so it took time to gather 10,000+ dataset (images), with various augmentations, preprocessing parameters.
- Annotations for the gathered dataset, along with the labelling of required classes is done.
- Dataset collection, Annotating, and training of the custom model to generate the required .pt files is done with Roboflow software.
- Trained the Dataset with batch size of 16 and with 50 epochs.
- Confusion Matrix for Dangerous Behaviour Detection
  
  ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/fd6a1952-c8df-456f-81b7-b14f478cb789)
  
- Confusion Matrix for Driver's Eye Closure Detection

  ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/8a1523a4-07bb-4b93-944f-bbccb9435375)

- Confusion Matrix for Facial Expression Analysis

  ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/f35a937d-cf68-42ea-99f1-18d3987e3c7a)

- Output for Driver's Eye Closure Detection
  - Drowsiness/Fatigueness is recognized from the Eye Status (Open, Closed, Half Open) in front of the camera. Here, only the two classes are displayed (Focused and Sleepy).
  - Based on the real-time drowsiness detection, when the driver feels drowsy, the system detects and takes safety measures such as an indication to the driver.
 
    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/e06b6a13-bbc4-4ef5-9622-aba50326628d)
    
    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/173ffa15-29c4-4db1-b242-e31c79b18339)

- Output for Dangerous Behaviour Detection
  - Distraction is recognized from the custom objects I have used such as Mobile Phone and Bottle in front of the camera. Here, only the two classes are displayed (Mobile and Drinking).
 
    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/ae9374b0-91ab-4756-93e5-e8d72bafec6f)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/488d6e5a-01ac-4207-91e2-cc0c17337696)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/582d9231-68d8-4801-bed0-2df9014332a6)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/dc39200f-1d4e-4b80-b5d6-cb3e712dc483)

- Output for Facial Expression Analysis
  - Facial emotion is recognized from my expressions in front of the camera. Here, only the two emotions are displayed (Nervous and Neutral).
  - Based on this real-time emotion detection, when the driver is nervous for a prolonged period of time, this indicates danger situation such as vehicle interruption by intruders (Anti-theft recognition).

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/d6ccfdb2-73fb-49e5-bd50-47651c28a043)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/449547a3-b1c5-4e20-bf21-c7c552747497)

- Output for Driver's Head Pose Estimation
  - Head Pose estimation is indirectly connected to the Driver Distraction Scenario. When the Driver’s head position is wavery without looking straight, the system indicates a warning to the driver.

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/9d37a807-9792-4764-ae0f-90e3cc033ca6)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/05f45b13-cc2f-46cc-a141-646e6b07bd2c)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/cfc5cfa3-8bc0-4c69-89f5-143559dc3f4a)


    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/ee32a0f6-abb6-4a3d-a3da-24e4c5f11e78)

    ![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/1787bfb4-5ebb-45f8-b0a8-ada8b505b2f6)
    
## Results for Hardware part of Smart Driver Monitoring System
Having completed the software implementation for my Smart Driver Monitoring System, I am now transitioning to the hardware aspect of the project. Specifically, my focus is on manipulating the Controller Area Network (CAN) bus signals generated by various Electronic Control Units (ECUs) in the vehicle. My goal is to override these CAN bus signals and generate new signals that align with the specific functionalities required for my driver monitoring system.

### Steps to be Followed

- Step-1: Tapping CAN Signals from various ECU’s via OBD-II port
- Step-2: Recognizing and Understanding the Pattern of the CAN Signals generated (Future Work)
- Step-3: Over-ride the CAN Signals for achieving Autonomy (Future Work)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/cd6aa4ca-ce9b-4b95-b753-62ca45bcc1ae)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/d59ac5e1-9e61-4cc7-afe9-4b98a2a777f9)

#### Automatic Vehicle control in the case of Driver losing full control:

- I tapped the CAN signals generated from the steering module's CAN port using a Logic Analyzer and Saleae Logic 2 Software.
- From the car's OBD port, using an OBD scanner, I obtained the car's input performance readings for analysis purposes.

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/27b593fe-5e1b-4f4f-aa1c-050cc7ea8de0)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/8a4e53bf-a9cd-49c6-96f7-1285a1f8639a)

#### Hardware Interfacing - Accessing CAN BUS data from Shift Desire Car’s OBD Port:

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/4633b405-ec26-4cc9-b1c7-712df03d22ec)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/cc36a2ec-e724-43d6-91d6-0801c665eec0)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/2e31bb58-0991-4926-bcde-51e2d3db08fa)

#### Generated CAN Signal:

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/1ea21d8a-1b6e-4fee-978c-b03f3646b743)

#### CAN Signals obtained in the software along with their address:

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/deb7dc6f-5acf-4724-b3d6-48c1a103866a)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/6c286e58-29e9-4b51-a6e3-9c3e061868a8)

** The highlighted CAN signal packets in violet color indicates the newly generated CAN Data in real-time as we adjust various input controls in the Vehicle, as like left steer, right steer, Turn on Stereo, Appling Brake, etc.,

** Currently, I am at the testing phase and have completed analyzing the behavior of CAN signals generated in the Shift Desire car on various input trials such as left steer, right steer, turning on the stereo, applying the brake, etc. By analyzing these data, I will be mimicking the CAN signals and writing the CAN signals for the specific function via the OBD-II port of the vehicle, to get actuated based on the driver’s behavior detected via the Driver Monitoring System software I developed. (Future Work)

# REAL-TIME DEPLOYMENT (FUTURE WORK)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/b2325a4c-1b45-4cab-a9b9-f2c11c4c547c)

![image](https://github.com/lakshminarayanan-kk/Smart-Driver-Monitoring-System-AutoDrive/assets/170000853/a819702e-6f15-493d-867c-5bd2c9e9c406)






















