from analyzer.detector.sagital.heel_lift_detector import HeelLiftDetector
from analyzer.detector.error_detector import PoseLandmark as l

def fake_kps_normal():
    """Talones en contacto con el suelo"""
    kps = [{'x': 0.5, 'y': 0.8, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_HEEL]['y'] = 0.95
    kps[l.LEFT_FOOT_INDEX]['y'] = 0.96
    kps[l.RIGHT_HEEL]['y'] = 0.95
    kps[l.RIGHT_FOOT_INDEX]['y'] = 0.96
    return kps

def fake_kps_left_lift():
    """Solo el talón izquierdo está elevado"""
    kps = [{'x': 0.5, 'y': 0.8, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_HEEL]['y'] = 0.90
    kps[l.LEFT_FOOT_INDEX]['y'] = 0.96
    kps[l.RIGHT_HEEL]['y'] = 0.95
    kps[l.RIGHT_FOOT_INDEX]['y'] = 0.96
    return kps

def fake_kps_both_lift():
    """Ambos talones elevados"""
    kps = [{'x': 0.5, 'y': 0.8, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_HEEL]['y'] = 0.89
    kps[l.LEFT_FOOT_INDEX]['y'] = 0.96
    kps[l.RIGHT_HEEL]['y'] = 0.88
    kps[l.RIGHT_FOOT_INDEX]['y'] = 0.96
    return kps

def print_test_result(name, result):
    print(f"[{name}]")
    print(result)
    print("")

def main():
    # Caso normal (sin error)
    kps = fake_kps_normal()
    detector = HeelLiftDetector(kps)
    result = detector.evaluate()
    print_test_result("Talones normales (esperado 'none')", result)

    # Caso con elevación izquierda
    kps = fake_kps_left_lift()
    detector = HeelLiftDetector(kps)
    result = detector.evaluate()
    print_test_result("Talón izquierdo elevado (esperado 'left')", result)

    # Caso con ambos talones elevados
    kps = fake_kps_both_lift()
    detector = HeelLiftDetector(kps)
    result = detector.evaluate()
    print_test_result("Ambos talones elevados (esperado 'both')", result)

if __name__ == "__main__":
    main()
