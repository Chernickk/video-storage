from datetime import timedelta

from manager.video_manager import VideoManager
from settings import VIDEO_DIR


if __name__ == '__main__':
    video_manager = VideoManager(video_path=VIDEO_DIR,
                                 delete_old=False,
                                 interval=timedelta(minutes=30))
    video_manager.start()
