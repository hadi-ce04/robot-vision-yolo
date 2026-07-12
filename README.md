# Robot Vision System using YOLO

A real-time computer vision system engineered for robotic perception, utilizing the **YOLO (You Only Look Once)** deep learning framework and **OpenCV**. This project enables a robot to interpret its environment by detecting and labeling everyday household and office objects dynamically via a live camera stream.

---

## 🚀 Features
* **Real-Time Object Detection:** Low-latency inference ideal for edge computing and robotic platforms.
* **Stream-Optimized Inference:** Utilizes generator-based streaming (`stream=True`) to maintain minimal memory overhead and maximize FPS.
* **Auto-Annotated Visualization:** Dynamically overlays bounding boxes, class labels, and confidence scores onto the live video feed.

## 🛠️ Tech Stack & Skills
* **Language:** Python
* **Libraries:** OpenCV (`opencv-python`), Ultralytics (`ultralytics`)
* **DevOps / Tools:** Git, GitHub, Virtual Environments (`venv`)

---

## 🔧 Installation & Setup

Follow these steps to get the vision system running locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/hadi-ce04/robot-vision-yolo.git](https://github.com/hadi-ce04/robot-vision-yolo.git)
cd robot-vision-yolo

# Create the environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

python vision_robot.py

🧠 How It Works
Frame Capture: OpenCV hooks into the default system hardware camera, capturing live video frames at a hardware-defined frame rate.

Deep Learning Processing: Each raw frame matrix is sent directly into a pre-trained convolutional neural network (YOLO), which extracts features to predict object bounding box coordinates and classification probabilities.

Rendering Layer: Bounding boxes and confidence percentages are rendered back onto the frame vector before being outputted onto a dedicated display window.
