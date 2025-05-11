from analyzer.detector.sagital.trunk_inclination_detector import TrunkInclinationDetector
from analyzer.detector.error_detector import PoseLandmark as l

def fake_kps_neutra():
    """Columna recta vertical (ángulo cercano a 0°)"""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.3, 0.3
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.7, 0.7
    return kps

def fake_kps_flexion():
    """Columna inclinada hacia delante (ángulo mayor)"""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_SHOULDER]['x'], kps[l.RIGHT_SHOULDER]['x'] = 0.3, 0.3
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.7, 0.7
    kps[l.LEFT_HIP]['x'], kps[l.RIGHT_HIP]['x'] = 0.55, 0.55
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.8, 0.8
    return kps

def fake_kps_extension():
    """Columna inclinada hacia atrás"""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_SHOULDER]['x'], kps[l.RIGHT_SHOULDER]['x'] = 0.1, 0.1
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.65, 0.65
    kps[l.LEFT_HIP]['x'], kps[l.RIGHT_HIP]['x'] = 0.6, 0.6
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.85, 0.85
    return kps

def print_test_result(name, result):
    print(f"[{name}]")
    print(result)
    print("")

def main():
    # Columna neutral
    kps = fake_kps_neutra()
    detector = TrunkInclinationDetector(kps)
    result = detector.evaluate()
    print_test_result("Columna neutral (esperado False)", result)

    # Columna con flexión
    kps = fake_kps_flexion()
    detector = TrunkInclinationDetector(kps)
    result = detector.evaluate()
    print_test_result("Columna en flexión anterior (esperado True)", result)

    # Columna con extensión
    kps = fake_kps_extension()
    detector = TrunkInclinationDetector(kps)
    result = detector.evaluate()
    print_test_result("Columna en hiperextensión (esperado True)", result)

if __name__ == "__main__":
    main()
