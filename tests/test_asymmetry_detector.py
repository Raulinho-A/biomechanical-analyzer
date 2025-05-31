from analyzer.detector.coronal.asymmetry_detector import AsymmetryDetector
from analyzer.detector.error_detector import PoseLandmark as l

def fake_kps_symmetric():
    """Postura completamente alineada (sin asimetría)"""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.7, 0.7
    kps[l.LEFT_KNEE]['x'], kps[l.RIGHT_KNEE]['x'] = 0.4, 0.6
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.3, 0.3
    return kps

def fake_kps_hip_asymmetry():
    """Una cadera más baja que la otra (asimetría de pelvis)"""
    kps = fake_kps_symmetric()
    kps[l.LEFT_HIP]['y'] = 0.65
    return kps

def fake_kps_shoulder_asymmetry():
    """Un hombro más caído que el otro"""
    kps = fake_kps_symmetric()
    kps[l.RIGHT_SHOULDER]['y'] = 0.35
    return kps

def print_test_result(name, result):
    print(f"[{name}]")
    print(result)
    print("")

def main():
    # Test 1: Sin asimetría
    kps = fake_kps_symmetric()
    detector = AsymmetryDetector(kps)
    result = detector.evaluate()
    print_test_result("Simetría completa (esperado False)", result)

    # Test 2: Asimetría de cadera
    kps = fake_kps_hip_asymmetry()
    detector = AsymmetryDetector(kps)
    result = detector.evaluate()
    print_test_result("Asimetría de cadera (esperado True)", result)

    # Test 3: Asimetría de hombros
    kps = fake_kps_shoulder_asymmetry()
    detector = AsymmetryDetector(kps)
    result = detector.evaluate()
    print_test_result("Asimetría de hombros (esperado True)", result)

if __name__ == "__main__":
    main()
