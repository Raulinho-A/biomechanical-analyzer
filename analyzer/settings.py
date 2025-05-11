from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJ_ROOT = Path(__file__).resolve().parents[1]

# Data paths
DATA_DIR = PROJ_ROOT / "data"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RAW_DATA_DIR = DATA_DIR / "raw"

# Planos
PLANOS_RECORDING = RAW_DATA_DIR / "planos-1.0"
PLANO_CORONAL = PLANOS_RECORDING / "coronal"
PLANO_SAGINTAL = PLANOS_RECORDING / "sagital"
PLANO_CUASI_SAGITAL = PLANOS_RECORDING / "cuasi-sagital"

# Processed
KEYPOINTS = INTERIM_DATA_DIR / 'keypoints'

# Raw
DEMOS = RAW_DATA_DIR / 'demos'

# Model paths
MODELS_DIR = PROJ_ROOT / "models"
MEDIAPIPE_MODEL_PATH = MODELS_DIR / "mediapipe" / "pose_landmarker_heavy.task"

# Other paths
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"