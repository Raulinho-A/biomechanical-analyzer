from analyzer.detector.coronal.valgo_detector import ValgoDetector
from analyzer.detector.posture_error_detector import PoseLandmark as l

def fake_kps_plano():
    """Todos los puntos son iguales → debería dar NaN y valgo=False."""
    return [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]

def fake_kps_realista():
    """Simula valgo: rodillas más cerca que tobillos, plano coronal."""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_HIP]['x'], kps[l.LEFT_KNEE]['x'], kps[l.LEFT_ANKLE]['x'] = 0.40, 0.42, 0.42
    kps[l.RIGHT_HIP]['x'], kps[l.RIGHT_KNEE]['x'], kps[l.RIGHT_ANKLE]['x'] = 0.60, 0.54, 0.58
    kps[l.LEFT_HIP]['y'], kps[l.LEFT_KNEE]['y'], kps[l.LEFT_ANKLE]['y'] = 0.5, 0.6, 0.7
    kps[l.RIGHT_HIP]['y'], kps[l.RIGHT_KNEE]['y'], kps[l.RIGHT_ANKLE]['y'] = 0.5, 0.6, 0.7
    return kps

def extremely_fake_kps():
    """Caso forzado: rodillas muy separadas pero ángulo aún bajo."""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]

    kps[l.LEFT_KNEE]['x'] = 0.40
    kps[l.RIGHT_KNEE]['x'] = 0.60
    kps[l.LEFT_ANKLE]['x'] = 0.45
    kps[l.RIGHT_ANKLE]['x'] = 0.55

    kps[l.LEFT_KNEE]['y'] = 0.6
    kps[l.RIGHT_KNEE]['y'] = 0.6
    kps[l.LEFT_ANKLE]['y'] = 0.7
    kps[l.RIGHT_ANKLE]['y'] = 0.7

    kps[l.LEFT_HIP]['x'], kps[l.RIGHT_HIP]['x'] = 0.42, 0.58
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.5, 0.5

    return kps

def print_test_result(name, result):
    print(f"[{name}]")
    print(result)
    print("")

def main():
    # Test 1: Todos los puntos iguales
    kps = fake_kps_plano()
    detector = ValgoDetector(kps)
    result = detector.evaluate()

    print_test_result("TEST CON TODOS LOS PUNTOS IGUALES", result)

    # Test 2: Valgo simulado
    kps = fake_kps_realista()
    detector = ValgoDetector(kps)
    result = detector.evaluate()

    print_test_result("TEST VALGO CON FAKE DATA REALISTA", result)

    # Test 3: Caso extremo no realista
    kps = extremely_fake_kps()
    detector = ValgoDetector(kps)
    result = detector.evaluate()
    print_test_result("TEST EXTREMO (NO REAL)", result)

if __name__ == "__main__":
    main()