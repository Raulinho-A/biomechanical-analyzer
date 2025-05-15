from analyzer.detector.error_detector import PoseLandmark, PostureErrorDetector
from analyzer.config.thresholds import (
    ASYMMETRY_HIP_Y_THRESHOLD,
    ASYMMETRY_KNEE_X_THRESHOLD,
    ASYMMETRY_SHOULDER_Y_THRESHOLD
)

class AsymmetryDetector(PostureErrorDetector):
    def evaluate(self):
        left_hip_y = self.get_point(PoseLandmark.LEFT_HIP)[1]
        right_hip_y = self.get_point(PoseLandmark.RIGHT_HIP)[1]

        left_knee_x = self.get_point(PoseLandmark.LEFT_KNEE)[0]
        right_knee_x = self.get_point(PoseLandmark.RIGHT_KNEE)[0]

        left_shoulder_y = self.get_point(PoseLandmark.LEFT_SHOULDER)[1]
        right_shoulder_y = self.get_point(PoseLandmark.RIGHT_SHOULDER)[1]

        hip_delta_y = abs(left_hip_y - right_hip_y)
        knee_delta_x = abs(left_knee_x - right_knee_x)
        shoulder_delta_y = abs(left_shoulder_y - right_shoulder_y)

        hip_asymmetry = hip_delta_y > ASYMMETRY_HIP_Y_THRESHOLD
        knee_asymmetry = knee_delta_x > ASYMMETRY_KNEE_X_THRESHOLD
        shoulder_asymmetry = shoulder_delta_y > ASYMMETRY_SHOULDER_Y_THRESHOLD

        return {
            "hip_delta_y": hip_delta_y,
            "hip_asymmetry_detected": hip_asymmetry,

            "knee_delta_x": knee_delta_x,
            "knee_asymmetry_detected": knee_asymmetry,

            "shoulder_delta_y": shoulder_delta_y,
            "shoulder_asymmetry_detected": shoulder_asymmetry,

            "overall_asymmetry_detected": hip_asymmetry or knee_asymmetry or shoulder_asymmetry
        }
