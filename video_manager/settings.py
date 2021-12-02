import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
VIDEO_DIR = os.path.join(BASE_DIR.parent, 'video')

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
FPS = 15
