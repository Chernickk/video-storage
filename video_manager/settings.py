import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = os.path.join(BASE_DIR.parent.parent, 'video')

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
FPS = 15
DB_URL = f"postgresql+psycopg2://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/video"
