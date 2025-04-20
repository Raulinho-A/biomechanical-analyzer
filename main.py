import json

from analyzer.vision.extract_keypoints import extract_pose_landmarks
from analyzer.config import RAW_DATA_DIR

video_path = RAW_DATA_DIR / "record_01.mp4"

keypoints = extract_pose_landmarks(str(video_path))

print(f"Se extrajeron keypoints de {len(keypoints)} frames")

output_json = RAW_DATA_DIR / "record_01_keypoints.json"
with open(output_json, "w") as f:
    json.dump(keypoints, f, indent=2)

print(f"Keypoints guardados en: {output_json}")

