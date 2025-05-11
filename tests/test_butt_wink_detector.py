from analyzer.detector.sagital.butt_wink_detector import ButtWinkDetector
from analyzer.detector.error_detector import PoseLandmark as l

def fake_kps_normal():
    """Sentadilla controlada, buena técnica. Ángulos amplios."""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.3, 0.3
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.6, 0.6
    kps[l.LEFT_KNEE]['y'], kps[l.RIGHT_KNEE]['y'] = 0.75, 0.75
    kps[l.LEFT_ANKLE]['y'], kps[l.RIGHT_ANKLE]['y'] = 0.9, 0.9
    return kps

def fake_kps_solo_profunda():
    """Sentadilla profunda, pero sin colapso del tronco."""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.3, 0.3
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.8, 0.8
    kps[l.LEFT_KNEE]['y'], kps[l.RIGHT_KNEE]['y'] = 0.85, 0.85
    kps[l.LEFT_ANKLE]['y'], kps[l.RIGHT_ANKLE]['y'] = 0.95, 0.95
    return kps

def fake_kps_solo_colapso():
    """Tronco colapsado, pero rodillas no muy flexionadas."""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]
    kps[l.LEFT_SHOULDER]['x'], kps[l.RIGHT_SHOULDER]['x'] = 0.25, 0.25
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.25, 0.25
    kps[l.LEFT_HIP]['x'], kps[l.RIGHT_HIP]['x'] = 0.5, 0.5
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.6, 0.6
    kps[l.LEFT_KNEE]['y'], kps[l.RIGHT_KNEE]['y'] = 0.7, 0.7
    kps[l.LEFT_ANKLE]['y'], kps[l.RIGHT_ANKLE]['y'] = 0.85, 0.85
    return kps

def fake_kps_butt_wink():
    """Sentadilla profunda + colapso de tronco → butt wink probable."""
    kps = [{'x': 0.5, 'y': 0.5, 'z': 0, 'visibility': 0.99} for _ in range(33)]

    # Tronco inclinado
    kps[l.LEFT_SHOULDER]['x'], kps[l.RIGHT_SHOULDER]['x'] = 0.3, 0.3
    kps[l.LEFT_SHOULDER]['y'], kps[l.RIGHT_SHOULDER]['y'] = 0.70, 0.70
    # Cadera baja y centrada
    kps[l.LEFT_HIP]['x'], kps[l.RIGHT_HIP]['x'] = 0.65, 0.65
    kps[l.LEFT_HIP]['y'], kps[l.RIGHT_HIP]['y'] = 0.85, 0.85
    # Rodilla más al frente (más `x`) para cerrar ángulo
    kps[l.LEFT_KNEE]['x'], kps[l.RIGHT_KNEE]['x'] = 0.4, 0.4
    kps[l.LEFT_KNEE]['y'], kps[l.RIGHT_KNEE]['y'] = 0.78, 0.78
    # Tobillo aún más al frente
    kps[l.LEFT_ANKLE]['x'], kps[l.RIGHT_ANKLE]['x'] = 0.5, 0.5
    kps[l.LEFT_ANKLE]['y'], kps[l.RIGHT_ANKLE]['y'] = 0.95, 0.95

    return kps

def print_test_result(name, result):
    print(f"[{name}]")
    print(result)
    print("")

def main():
    # Caso 1: Sentadilla normal
    kps = fake_kps_normal()
    detector = ButtWinkDetector(kps)
    result = detector.evaluate()
    print_test_result("Caso 1: Sentadilla normal (esperado False)", result)

    # Caso 2: Sentadilla profunda sin colapso
    kps = fake_kps_solo_profunda()
    detector = ButtWinkDetector(kps)
    result = detector.evaluate()
    print_test_result("Caso 2: Solo profundidad (esperado False)", result)

    # Caso 3: Colapso sin profundidad
    kps = fake_kps_solo_colapso()
    detector = ButtWinkDetector(kps)
    result = detector.evaluate()
    print_test_result("Caso 3: Solo colapso (esperado False)", result)

    # Caso 4: Butt wink completo (profundidad + colapso)
    kps = fake_kps_butt_wink()
    detector = ButtWinkDetector(kps)
    result = detector.evaluate()
    print_test_result("Caso 4: Butt wink (esperado True)", result)

if __name__ == "__main__":
    main()
