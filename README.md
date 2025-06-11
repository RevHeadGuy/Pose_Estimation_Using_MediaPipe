# Pose_Estimation_Using_MediaPipe

This project performs real-time human **pose detection** using **MediaPipe** and **OpenCV**. It detects key body landmarks from a webcam, image, or video, and includes utilities for angle calculation, repetition counting (e.g. squats), and visualization.

pose_estimation_project/
│
├── main.py # Real-time webcam pose detection
├── image_pose.py # Static image pose detection
├── video_pose.py # Video file pose detection
├── pose_utils.py # Landmark drawing, angle calculation, counters
├── requirements.txt # Python dependencies
├── README.md # Project overview

## 🛠 Features

- 🔍 Real-time pose detection using webcam
- 🖼 Static image and video processing
- 📐 Joint angle calculation (e.g. knee, elbow)
- 🧮 Squat repetition counter logic
- 📊 Easily extendable for feedback, CSV logging, or exercise analysis

# Install Requirements :

pip install -r requirements.txt

# Run Webcam-based Pose Estimation : 

python main.py

# Run on an Image :

python image_pose.py

# Run on a Video File :

python video_pose.py




