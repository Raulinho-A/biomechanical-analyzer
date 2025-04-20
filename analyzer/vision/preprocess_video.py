import cv2

from analyzer.config import RAW_DATA_DIR

OUTPUT_PATH = RAW_DATA_DIR / 'record_01.mp4'

cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)

if not cap.isOpened():
    raise IOError(f"Cannnot open camera")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow('Record:', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video guardado en: {OUTPUT_PATH}")