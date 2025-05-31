import cv2
from analyzer.settings import RAW_DATA_DIR

class VideoRecorder:
    def __init__(self, output_name: str = 'record_01.mp4', camera_index=0):
        self.output_path = RAW_DATA_DIR / output_name
        self.cap = cv2.VideoCapture(camera_index)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(str(self.output_path), fourcc, self.fps, (self.frame_width, self.frame_height))

        if not self.cap.isOpened():
            raise IOError("Cannot open camera")
        
        self.is_paused = False

    def record(self):
        print(f"Grabando video en: {self.output_path}")
        print("Presiona 'p' para pausar/reanudar, 'ESC' para terminar.")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            if not self.is_paused:
                self.out.write(frame)

            status_text = 'Pausado' if self.is_paused else 'Grabando'
            frame_display = frame.copy()
            cv2.putText(frame_display, status_text, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Recording (p=Pause, ESC=Stop)', frame_display)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break
            elif key == ord('p'):
                self.is_paused = not self.is_paused
                print(f"{'Pausa' if self.is_paused else 'Reanudado'}")    
        self.release()

    def release(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
        print(f"Video guardado en: {self.output_path}")


'''
- Agregar manejo de excepciones:
Por si en medio del grabado hay un error (desconexión de cámara, etc.).
- Agregar un método pause() y resume() separados:
Para hacerlo más orientado a objetos desde fuera, para controlar
la pausa desde otro código externo en vez del teclado
- Logs o historial de pausas: Guardar un listado de cuándo se pausó
y se reanudó para analizar después.
'''