from analyzer.vision.capture import VideoRecorder
from analyzer.vision.keypoints.pose_extractor import PoseExtractor
from analyzer.vision.keypoints.pose_drawer import PoseDrawer
from analyzer.config import DEMOS, KEYPOINTS

def main():
    ## Recording
    # recorder = VideoRecorder(output_name='demo_01.mp4')
    # recorder.record()

    ## Extracting
    # video_path = DEMOS / 'demo_01.mp4'
    # extractor = PoseExtractor(video_path=video_path)
    # extractor.extract(show=True)

    ## Drawing
    video_path = DEMOS / 'demo_01.mp4'
    keypoints_json = KEYPOINTS / 'demo_01_keypoints.json'

    drawer = PoseDrawer(video_path=video_path, keypoints_json=keypoints_json)
    drawer.draw_and_save(show=True)

if __name__ == "__main__":
    main()