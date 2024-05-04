# Hand Gesture Controlled Mouse Cursor
## Overview
This project is aimed at controlling the mouse cursor using hand gestures captured through a webcam. It utilizes computer vision techniques and the MediaPipe library to detect hand landmarks and translate them into mouse movements and actions.

## Features
Real-time hand gesture detection and tracking.

Mapping hand landmarks to screen coordinates for mouse cursor control.

Performing click operations based on hand gestures.
## Requirements
Python 3.x

OpenCV (pip install opencv-python)

Mediapipe (pip install mediapipe)

PyAutoGUI (pip install pyautogui)

## Usage
Clone this repository to your local machine.

Install the required dependencies using pip.

Run the handMouse.py script.

Position your hand in front of the webcam, and the program will track your hand movements and translate them into mouse actions.
## How it Works
The program captures frames from the webcam feed.
It uses the MediaPipe library to detect hand landmarks in each frame.
Hand landmarks are mapped to screen coordinates to control the mouse cursor.
Hand gestures such as closing the index finger and thumb trigger mouse click operations.
