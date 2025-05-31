from analyzer.detector.angle_utils import calculate_angle
from analyzer.detector.error_detector import PoseLandmark, PostureErrorDetector
from analyzer.config.thresholds import (
    BUTT_WINK_TRUNK_THIGH_ANGLE_THRESHOLD,
    BUTT_WINK_KNEE_ANGLE_THRESHOLD
)
import numpy as np

class ButtWinkDetector(PostureErrorDetector):
    def evaluate(self):
        # Puntos clave
        shoulder_center = self._average_point(PoseLandmark.LEFT_SHOULDER, PoseLandmark.RIGHT_SHOULDER)
        hip_center = self._average_point(PoseLandmark.LEFT_HIP, PoseLandmark.RIGHT_HIP)
        knee_center = self._average_point(PoseLandmark.LEFT_KNEE, PoseLandmark.RIGHT_KNEE)
        ankle_center = self._average_point(PoseLandmark.LEFT_ANKLE, PoseLandmark.RIGHT_ANKLE)

        # Heurística 1: ángulo de flexión de rodilla (profundidad)
        knee_angle = calculate_angle(hip_center, knee_center, ankle_center)

        # Heurística 2: ángulo de colapso entre tronco y muslo
        trunk_thigh_angle = calculate_angle(shoulder_center, hip_center, knee_center)

        # Feature: relación de inclinación sobre profundidad
        inclinacion_profundidad_ratio = trunk_thigh_angle / knee_angle if knee_angle != 0 else float('inf')

        butt_wink_detected = (
            knee_angle < BUTT_WINK_KNEE_ANGLE_THRESHOLD and
            trunk_thigh_angle < BUTT_WINK_TRUNK_THIGH_ANGLE_THRESHOLD
        )

        return {
            "knee_angle": knee_angle,
            "trunk_thigh_angle": trunk_thigh_angle,
            "inclinacion_profundidad_ratio": inclinacion_profundidad_ratio,
            "butt_wink_detected": butt_wink_detected
        }
    
    def _average_point(self, idx1, idx2):
        p1 = np.array(self.get_point(idx1))
        p2 = np.array(self.get_point(idx2))
        return ((p1 + p2) / 2).tolist()