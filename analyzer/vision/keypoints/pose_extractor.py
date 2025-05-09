import cv2
import json
import mediapipe as mp
from mediapipe.tasks import python, vision
from pathlib import Path
from analyzer.config import MEDIAPIPE_MODEL_PATH, KEYPOINTS

BaseOptions = python.BaseOptions
PoseLandmarker = vision.PoseLandmarker
PoseLandmarkerOptions = vision.PoseLandmarkerOptions
VisionRunningMode = vision.RunningMode

class PoseExtractor:
    def __init__(self, video_path: str, output_json: str = None):
        self.video_path = Path(video_path)
        self.output_json = Path(output_json) if output_json else (KEYPOINTS / f"{self.video_path.stem}_keypoints.json")
        self.model_path = MEDIAPIPE_MODEL_PATH

    def extract(self, show=False):
        cap = cv2.VideoCapture(str(self.video_path))
        if not cap.isOpened():
            raise IOError(f"Cannot open video: {self.video_path}")
        
        options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(self.model_path)),
            running_mode=VisionRunningMode.VIDEO,
            num_poses=1,
            min_pose_detection_confidence=0.5,
            min_pose_presence_confidence=0.5,
            min_tracking_confidence=0.6,
            output_segmentation_masks=False
        )

        all_landmarks = []
        frame_index = 0
        fps = cap.get(cv2.CAP_PROP_FPS)

        drawing_spec = mp.solutions.drawing_styles.get_default_pose_landmarks_style()

        with PoseLandmarker.create_from_options(options) as landmarker:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
                timestamp = int((frame_index / fps) * 1000)
                result = landmarker.detect_for_video(mp_image, timestamp)

                if result.pose_landmarks:
                    keypoints = [{
                        "x": lm.x,
                        "y": lm.y,
                        "z": lm.z,
                        "visibility": lm.visibility
                    } for lm in result.pose_landmarks[0]]
                    all_landmarks.append(keypoints)

                    if show:
                        mp.solutions.drawing_utils.draw_landmarks(
                            frame, result.pose_landmarks[0],
                            mp.solutions.pose.POSE_CONNECTIONS,
                            landmark_drawin_spec=drawing_spec
                        )
                    else:
                         all_landmarks.append([])

                    if show:
                        cv2.imshow('Pose Extracting', frame)
                        if cv2.waitKey(1) & 0xFF == 27:
                            print("Debug visual interrumpido")
                            break
                    frame_index += 1

        cap.release()
        if show:
            cv2.destroyAllWindows()

        self.save_to_json(all_landmarks)
        return all_landmarks
    
    def save_to_json(self, data):
        with open(self.output_json, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Keypoints dados en: {self.output_json}")

