from analyzer.vision.capture import VideoRecorder
from analyzer.vision.keypoints.pose_extractor import PoseExtractor
from analyzer.config import DEMOS

def main():
    ## Recording
    # recorder = VideoRecorder(output_name='demo_01.mp4')
    # recorder.record()

    ## Extracting
    video_path = DEMOS / 'demo_01.mp4'
    extractor = PoseExtractor(video_path=video_path)
    extractor.extract(show=True)
    
if __name__ == "__main__":
    main()