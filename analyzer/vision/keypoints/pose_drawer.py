import cv2
import json
from pathlib import Path
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from analyzer.settings import KEYPOINTS

class PoseDrawer:
    def __init__(self, video_path: str, keypoints_json: str, output_video: str = None):
        self.video_path = Path(video_path)
        self.keypoints_json = Path(keypoints_json)
        if output_video:
            self.output_video = Path(output_video)
        else:
            self.output_video = KEYPOINTS / f"{self.video_path.stem}_annotated.mp4"


    def draw_and_save(self, show=False):
        cap = cv2.VideoCapture(str(self.video_path))
        if not cap.isOpened():
            raise IOError(f"Cannot open video: {self.video_path}")
        
        with open(self.keypoints_json, 'r') as f:
            all_landmarks = json.load(f)

        fps = cap.get(cv2.CAP_PROP_FPS)

        ret, frame = cap.read()
        if not ret:
            raise IOError(f"Cannot read frames from: {self.video_path}")
        
        frame = self.make_square(frame)
        height, width = frame.shape[:2]

        cap.release()
        cap = cv2.VideoCapture(str(self.video_path))
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(str(self.output_video), fourcc, fps, (width, height))
        drawing_spec = mp.solutions.drawing_styles.get_default_pose_landmarks_style()

        frame_index = 0
        print(f"Guardando video anotado en: {self.output_video}...")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = self.make_square(frame)

            if frame_index < len(all_landmarks):
                keypoints = all_landmarks[frame_index]
                if keypoints:
                    pose_landmarks = []
                    for kp in keypoints:
                        landmark = landmark_pb2.NormalizedLandmark(
                            x=kp['x'],
                            y=kp['y'],
                            z=kp['z'],
                            visibility=kp['visibility']
                        )
                        pose_landmarks.append(landmark)

                    landmark_list = landmark_pb2.NormalizedLandmarkList(
                        landmark=pose_landmarks
                    )

                    mp.solutions.drawing_utils.draw_landmarks(
                        frame,
                        landmark_list,
                        mp.solutions.pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=drawing_spec
                    )

            out.write(frame)

            if show:
                cv2.imshow('Annotated Video', frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    print("Visualización interrumpida por usuario.")
                    break

            frame_index += 1

        cap.release()
        out.release()
        if show:
            cv2.destroyAllWindows()
        print(f"Video anotado guardado en: {self.output_video}")

    def make_square(self, image):
        """Recorta la imagen para que sea cuadrada, centrando el contenido."""
        height, width = image.shape[:2]
        size = min(height, width)
        top = (height - size) // 2
        left = (width - size) // 2
        cropped = image[top:top + size, left:left + size]
        return cropped