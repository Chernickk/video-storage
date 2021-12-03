import os
from datetime import timedelta, datetime
from threading import Thread
from time import sleep
from typing import List

from manager.utils import extract_name, extract_datetime, get_duration, merge_clips
from logs.logger import logger


class VideoManager(Thread):
    def __init__(self, video_path: str, delete_old: bool, interval: timedelta):
        self.video_path = video_path
        self.delete_old = delete_old
        self.interval = interval.total_seconds()
        super().__init__()

    def check_upload_progress(self, files: List[str], path) -> bool:
        for file in files:
            create_dt = datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file)))
            if datetime.now() - create_dt < timedelta(hours=1):
                logger.info('Обнаружены свежие файлы, пока не обьединяем')
                return True
        return False

    def delete_old_files(self, path: str, time_delta: timedelta) -> None:
        deleted = False
        for file in os.listdir(path):
            path_to_file = os.path.join(path, file)
            if not os.path.isdir(path_to_file):
                if datetime.fromtimestamp(os.path.getmtime(path_to_file)) < (datetime.now() - time_delta):
                    os.remove(path_to_file)
                    deleted = True
            else:
                self.delete_old_files(path_to_file, time_delta=time_delta)

        if deleted:
            logger.info('old files has been deleted')

    def merge_closest_clips(self, directory: str, files: List[str]) -> None:
        camera_names = set([extract_name(file) for file in files])
        for name in camera_names:
            named_clips = [file for file in files if extract_name(file) == name]
            while named_clips:
                files_to_merge = [named_clips.pop(0)]
                while named_clips:
                    next_clip_start_time = extract_datetime(named_clips[0])
                    last_clip_end_time = extract_datetime(files_to_merge[-1]) + get_duration(files_to_merge[-1])
                    if (next_clip_start_time - last_clip_end_time) < timedelta(minutes=10):
                        files_to_merge.append(named_clips.pop(0))
                    else:
                        break
                result_name = merge_clips(files_to_merge, os.path.join(self.video_path, directory, 'temp'),
                                          os.path.join(self.video_path, directory), car_license_table=directory)
                #  directory and car_license_table are same
                logger.info(f'File created: {result_name}')

    def run(self):
        while True:
            try:
                for directory in os.listdir(self.video_path):
                    temp_dir = os.path.join(self.video_path, directory, 'temp')
                    files = os.listdir(temp_dir)
                    files.sort()
                    if self.check_upload_progress(files, temp_dir):
                        break
                    self.merge_closest_clips(directory, files)
                if self.delete_old:
                    self.delete_old_files(self.video_path, timedelta(days=60))

            except Exception as error:
                logger.exception(f'{error}')

            finally:
                sleep(self.interval)
