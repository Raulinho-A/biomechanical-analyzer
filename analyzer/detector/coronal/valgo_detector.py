from analyzer.detector.angle_utils import calculate_angle
from analyzer.detector.error_detector import PoseLandmark, PostureErrorDetector
from analyzer.config.thresholds import VALGO_ANGLE_THRESHOLD, VALGO_RATIO_THRESHOLD
import numpy as np

class ValgoDetector(PostureErrorDetector):
    def evaluate(self):
        left_angle = calculate_angle(
            self.get_point(PoseLandmark.LEFT_HIP),
            self.get_point(PoseLandmark.LEFT_KNEE),
            self.get_point(PoseLandmark.LEFT_ANKLE)
        )
        right_angle = calculate_angle(
            self.get_point(PoseLandmark.RIGHT_HIP),
            self.get_point(PoseLandmark.RIGHT_KNEE),
            self.get_point(PoseLandmark.RIGHT_ANKLE)
        )

        knee_distance = self._euclidean_distance(PoseLandmark.LEFT_KNEE, PoseLandmark.RIGHT_KNEE)
        ankle_distance = self._euclidean_distance(PoseLandmark.LEFT_ANKLE, PoseLandmark.RIGHT_ANKLE)

        ratio = knee_distance / ankle_distance if ankle_distance != 0 else float('inf')

        left_valgo = left_angle < VALGO_ANGLE_THRESHOLD and ratio < VALGO_RATIO_THRESHOLD
        right_valgo = right_angle < VALGO_ANGLE_THRESHOLD and ratio < VALGO_RATIO_THRESHOLD

        left_severity = (1.0 - ratio) if left_valgo else 0.0
        right_severity = (1.0 - ratio) if right_valgo else 0.0

        valgo_detected_in = (
            "both" if left_valgo and right_valgo
            else "left" if left_valgo
            else "right" if right_valgo
            else "none"
        )

        return {
            "left_knee_angle": left_angle,
            "right_knee_angle": right_angle,
            "knee_to_ankle_ratio": ratio,
            "left_valgo": left_valgo,
            "right_valgo": right_valgo,
            "valgo_detected_in": valgo_detected_in,
            "left_valgo_severity": left_severity,
            "right_valgo_severity": right_severity
        }
    
    def _euclidean_distance(self, a, b):
        a = np.array(self.get_point(a))
        b = np.array(self.get_point(b))
        return np.linalg.norm(a - b)