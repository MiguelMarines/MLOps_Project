from pathlib import Path
import os

PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = PROJECT_DIR / "data"

def get_data_dir():
    env = os.getenv("ABS_DATA_DIR")
    if env:
        return Path(env)
    return DEFAULT_DATA_DIR
