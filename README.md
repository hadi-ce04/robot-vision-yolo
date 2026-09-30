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
