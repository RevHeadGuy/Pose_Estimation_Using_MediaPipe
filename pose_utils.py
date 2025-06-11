import cv2
import numpy as np
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# === Function: Draw landmarks on the image ===
def draw_landmarks(image, results):
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(255,0,0), thickness=2)
        )

# === Function: Get coordinates of a specific landmark ===
def get_landmark_coords(landmark, shape):
    h, w, _ = shape
    return int(landmark.x * w), int(landmark.y * h)

# === Function: Calculate angle between 3 points ===
def calculate_angle(a, b, c):
    """
    a, b, c: each a tuple of (x, y)
    Returns: angle at point b in degrees
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-8)
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

# === Function: Count repetitions using joint angle ===
def count_reps(angle, counter, stage, low_thresh=90, high_thresh=160):
    """
    angle: current angle of joint
    counter: current count
    stage: current stage ("up" or "down")
    Returns updated (counter, stage)
    """
    if angle > high_thresh:
        stage = "up"
    if angle < low_thresh and stage == "up":
        stage = "down"
        counter += 1
    return counter, stage

# === Function: Extract all landmark coordinates ===
def extract_landmarks(results, shape):
    if not results.pose_landmarks:
        return None
    h, w, _ = shape
    landmarks = []
    for lm in results.pose_landmarks.landmark:
        landmarks.append((int(lm.x * w), int(lm.y * h), lm.z))
    return landmarks
