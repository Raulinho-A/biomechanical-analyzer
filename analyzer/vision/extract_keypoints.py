import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from typing import List, Dict
from analyzer.config import MEDIAPIPE_MODEL_PATH

BaseOptions = python.BaseOptions
PoseLandmarker = vision.PoseLandmarker
PoseLandmarkerOptions = vision.PoseLandmarkerOptions
VisionRunningMode = vision.RunningMode

MODEL_PATH = MEDIAPIPE_MODEL_PATH

def extract_pose_landmarks(video_path: str) -> List[Dict]:
    all_landmarks = []

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannnot open video: {video_path}")

    options = PoseLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=MODEL_PATH),
        running_mode=VisionRunningMode.VIDEO,
        num_poses=1,
        min_pose_detection_confidence=0.5,
        min_pose_presence_confidence=0.5,
        min_tracking_confidence=0.6,
        output_segmentation_masks=False
    )

    with PoseLandmarker.create_from_options(options) as landmarker:
        frame_index = 0
        fps = cap.get(cv2.CAP_PROP_FPS)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            timestamp = int((frame_index / fps) * 1_000)
            result = landmarker.detect_for_video(mp_image, timestamp)

            if result.pose_landmarks:
                keypoints = []
                for landmark in result.pose_landmarks[0]:
                    keypoints.append({
                        "x": landmark.x,
                        "y": landmark.y,
                        "z": landmark.z,
                        "visibility": landmark.visibility
                    })
                all_landmarks.append(keypoints)
            else:
                all_landmarks.append([])

            frame_index += 1
    
        cap.release()
        return all_landmarks
