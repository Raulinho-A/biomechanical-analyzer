from analyzer.detector.angle_utils import calculate_angle
from analyzer.detector.error_detector import PoseLandmark, PostureErrorDetector
from analyzer.config.thresholds import TRUNK_INCLINATION_ANGLE_THRESHOLD
import numpy as np

class TrunkInclinationDetector(PostureErrorDetector):
    def evaluate(self):
        # Average shoulder and hip points
        shoulder_center = self._average_point(
            PoseLandmark.LEFT_SHOULDER, PoseLandmark.RIGHT_SHOULDER
        )
        hip_center = self._average_point(
            PoseLandmark.LEFT_HIP, PoseLandmark.RIGHT_HIP
        )

        vertical_reference = [shoulder_center[0], 1.0]

        trunk_angle = calculate_angle(vertical_reference, shoulder_center, hip_center)

        trunk_inclination_detected = trunk_angle > TRUNK_INCLINATION_ANGLE_THRESHOLD

        return {
            "trunk_inclination_angle": trunk_angle,
            "trunk_inclination_detected": trunk_inclination_detected
        }

    def _average_point(self, idx1, idx2):
        p1 = np.array(self.get_point(idx1))
        p2 = np.array(self.get_point(idx2))
        return ((p1 + p2) / 2).tolist()
    