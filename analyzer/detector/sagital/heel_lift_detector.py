from analyzer.detector.error_detector import PoseLandmark, PostureErrorDetector
from analyzer.config.thresholds import HEEL_LIFT_Y_THRESHOLD

class HeelLiftDetector(PostureErrorDetector):
    def evaluate(self):
        left_heel_y = self.get_point(PoseLandmark.LEFT_HEEL)[1]
        left_toe_y = self.get_point(PoseLandmark.LEFT_FOOT_INDEX)[1]

        right_heel_y = self.get_point(PoseLandmark.RIGHT_HEEL)[1]
        right_toe_y = self.get_point(PoseLandmark.RIGHT_FOOT_INDEX)[1]

        left_score = left_toe_y - left_heel_y
        right_score = right_toe_y - right_heel_y

        left_elevated = (left_heel_y < left_toe_y - HEEL_LIFT_Y_THRESHOLD)
        right_elevated = (right_heel_y < right_toe_y - HEEL_LIFT_Y_THRESHOLD)

        return {
            "left_heel_y": left_heel_y,
            "left_toe_y": left_toe_y,
            "right_heel_y": right_heel_y,
            "right_toe_y": right_toe_y,
            "heel_lift_score_left": left_score,
            "heel_lift_score_right": right_score,
            "left_heel_elevated": left_elevated,
            "right_heel_elevated": right_elevated,
            "heel_lift_detected_in": (
                "both" if left_elevated and right_elevated
                else "left" if left_elevated
                else "right" if right_elevated
                else "none"
            )
        }