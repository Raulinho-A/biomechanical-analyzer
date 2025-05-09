from analyzer.vision.capture import VideoRecorder

def main():
    recorder = VideoRecorder(output_name='demo_01.mp4')
    recorder.record()

if __name__ == "__main__":
    main()