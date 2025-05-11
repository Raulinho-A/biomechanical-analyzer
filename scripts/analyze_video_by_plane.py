import json
from pathlib import Path

from analyzer.detector.coronal.valgo_detector import ValgoDetector

KEYPOINTS_JSON_PATH = Path("data/interim/keypoints/demo_01_keypoints.json")

def load_keypoints(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)
    
def main():
    keypoints_frames = load_keypoints(KEYPOINTS_JSON_PATH)

    for i, frame in enumerate(keypoints_frames):
        if not frame:
            print(f"[Frame {i}] No keypoints detectados.")
            continue

        detector = ValgoDetector(frame)
        result = detector.evaluate()
        print(f"[Frame {i}] {result}")

if __name__ == "__main__":
    main()