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

# Errores técnicos
ERRORES_TECNICOS = RAW_DATA_DIR / "planos-1.0"
ERRORES_PLANO_CORONAL = ERRORES_TECNICOS / "coronal"
ERRORES_PLANO_SAGINTAL = ERRORES_TECNICOS / "sagital"
ERRORES_PLANO_CUASI_SAGITAL = ERRORES_TECNICOS / "cuasi-sagital"

# Model paths
MODELS_DIR = PROJ_ROOT / "models"
MEDIAPIPE_MODEL_PATH = MODELS_DIR / "mediapipe" / "pose_landmarker_heavy.task"

# Other paths
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"