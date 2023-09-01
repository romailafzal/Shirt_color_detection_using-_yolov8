# Shirt Color Detection Web Application
By Saeed Anwar, Romail Afzal, Muhammad Masoom, Arslan Anwar
# Contents
- [Introduction ](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#Usage)
- [Configuration](#Configuartion)

## Introduction
This project is a Django-based web application for real-time Shirt color detection using [YOLO](https://docs.ultralytics.com/) v8. The application allows users to upload images, capture images from their camera, and perform real-time shirt color detection on the camera feed. The detected shirts are highlighted in the images using bounding boxes.

## Features

- Upload and process images for shirt color detection.
- Capture images using your device's camera for real-time shirt color detection.
- Display the processed images with detected shirt color highlighted using bounding boxes.

## Requirements

- Django
- torch
- numpy
- Pillow
- opencv-python
- ultralytics

## Installation

1. Clone this repository to your local machine:git clone https://github.com/romailafzal/Shirt_color_detection_using-_yolov8

2. Create a virtual environment (optional but recommended):
   
   python3 -m venv venv
   source venv/bin/activate
   
3. Install the required dependencies:
   pip install -r requirements.txt

4. Run the Django development server:
  python manage.py runserver


5. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.
   8000 is the port use your port accordingly

## Usage

1. **Upload Photo:** Visit the upload page to select and upload an image from your local machine. The application will process the image and display it with the detected shirt color highlighted.

2. **Camera Stream:** Access the camera stream page to capture real-time images using your device's camera. The captured images will be processed for shirt color detection, and the results will be displayed.

3. **Detected Image:** View the processed image with detected shirt color highlighted.

4. **Real-Time Detection:** Use the real-time detection feature to stream live camera feed and see the detected shirt color in real time.

## Configuration

- The YOLO model weights are loaded from the path `/home/romail/ML1/trainning/SHIRT_DETECTION/v8best/best2.pt`. You can update this path to point to your trained YOLO weights.

## Note

- The application may require additional setup and configurations, especially related to camera access and YOLO model weights path.

## Acknowledgments

This project was inspired by the need for a simple and interactive Shirt Color detection web application.


