# 🤖 Robot Vision System

> **Giving a robot eyes. 👁️**

A real-time computer vision system built with **Python, YOLO and OpenCV** that allows a camera-equipped system to detect and identify objects in its environment.

The project explores a fundamental problem in robotics:

**How can a machine understand what it is looking at?**

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-111111?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Real-time detection · Computer Vision · Robotic Perception**

</div>

---

## 🎥 See It In Action

<!-- Replace this with a GIF/video once you have one -->

<p align="center">
  <img src="assets/demo.gif" width="800" alt="Robot Vision System Demo">
</p>

> 📹 **Coming soon:** A short demonstration of the system detecting objects through a live camera feed.

---

## 🧠 What Does It Actually Do?

The system takes a **live camera feed**, processes each frame through a pre-trained **YOLO object detection model**, and identifies objects in the environment.

For every detected object, the system can display:

- 🎯 Bounding box
- 🏷️ Object class
- 📊 Confidence score
- ⚡ Real-time visual feedback

In simple terms:


        📷 CAMERA
            │
            ▼
    ┌─────────────────┐
    │   OpenCV        │
    │  Frame Capture  │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │      YOLO       │
    │ Object Detection│
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   Detection     │
    │  + Confidence   │
    │  + Bounding Box │
    └────────┬────────┘
             │
             ▼
       🖥️ LIVE OUTPUT




       🚀 Features
👁️ Real-Time Object Detection

Processes frames from the system camera and performs object detection continuously.

⚡ Stream-Based Inference

Uses YOLO's stream=True inference mode to process results incrementally rather than unnecessarily storing the entire result set in memory.

🎯 Automatic Annotation

Detected objects are automatically visualized with:

Bounding boxes
Class labels
Confidence percentages
🧩 Robotics-Oriented Architecture

Although the current project focuses on perception, the system is designed around a concept that can become part of a larger autonomous robotics pipeline:

Perception → Decision Making → Control → Action
     ▲
     │
  This project
🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core application
👁️ OpenCV	Camera input & image processing
🎯 YOLO	Object detection
🧰 Ultralytics	YOLO implementation
📦 venv	Environment isolation
🔧 Git	Version control
⚙️ How It Works
1. 📷 Frame Capture

OpenCV connects to the default camera and continuously captures frames.

cap = cv2.VideoCapture(0)

Each frame becomes the input to the detection pipeline.

2. 🧠 Deep Learning Inference

The frame is passed to a pre-trained YOLO model.

YOLO analyzes the image and predicts:

Object
├── Class
├── Bounding Box
└── Confidence
3. 🎨 Visualization

The predictions are rendered back onto the original frame.

The resulting image gives the user an immediate visual representation of what the model sees.

4. 🔄 Repeat

The process continues frame-by-frame, creating a live detection experience.

🏗️ Architecture
🔧 Getting Started
Requirements
Python 3.x
A working webcam
Windows / macOS / Linux
1. Clone
git clone https://github.com/hadi-ce04/robot-vision-yolo.git

cd robot-vision-yolo
2. Create a virtual environment
python -m venv venv
3. Activate it

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Start the system
python vision_robot.py
🎮 Interacting With The System

Once running:

             CAMERA
                │
                ▼
        ┌───────────────┐
        │  Live Stream  │
        └───────┬───────┘
                │
        ┌───────▼───────┐
        │      YOLO     │
        └───────┬───────┘
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
    🪑 Chair   📱 Phone  🧑 Person
      92%        87%       99%

Move objects into the camera's field of view and watch the model identify them in real time.

📊 What I Learned

This project helped me understand that computer vision isn't simply about running a model and getting a prediction.

I learned about the complete pipeline:

Camera → Image → Model → Prediction → Visualization

More importantly, it gave me experience connecting a machine-learning model to a real-world input source rather than working only with static datasets.

It also introduced me to practical considerations around:

Real-time inference
Frame processing
Memory usage
Model predictions
Confidence thresholds
Computer vision pipelines
🔭 What's Next?

This project is currently focused on robotic perception.

The next step is to move from:

"The robot can see an object."

to:

"The robot understands what it sees and acts accordingly."

Potential future directions:

 🤖 Connect detection to a ROS2 pipeline
 🗺️ Add object tracking
 🎯 Improve detection stability
 📍 Estimate object position
 🧠 Connect perception to decision-making
 🦾 Use detections to trigger robotic actions
 ⚡ Explore edge-device deployment
💡 Why I Built This

I wanted to explore one of the building blocks behind autonomous robotics:

Perception.

Before a robot can make decisions about the world, it needs some way to understand what is around it.

This project is my first step toward building systems where software can see, interpret, and eventually interact with the physical world.

👨‍💻 Author
Hadi

Computer Engineering Student @ Epitech Paris

Interested in:

AI · Robotics · Computer Vision · Automation · Embedded Systems
