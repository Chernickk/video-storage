import os
from datetime import timedelta, datetime
from time import sleep
from typing import List

from settings import VIDEO_DIR
from manager.utils import extract_name, merge_clips, extract_datetime, get_duration


def check_upload_progress(files: List[str], path):
    for file in files:
        create_dt = datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file)))
        if create_dt - datetime.now() > timedelta(hours=1):
            return True
    return False


def delete_old_files(path: str, time_delta: timedelta):
    for file in os.listdir(path):
        path_to_file = os.path.join(path, file)
        if not os.path.isdir(path_to_file):
            if datetime.fromtimestamp(os.path.getmtime(path_to_file)) < (datetime.now() - time_delta):
                os.remove(path_to_file)
        else:
            delete_old_files(path_to_file, time_delta=time_delta)


while True:
    try:
        for directory in os.listdir(VIDEO_DIR):
            files = os.listdir(os.path.join(VIDEO_DIR, directory, 'temp'))
            files.sort()
            if check_upload_progress(files, os.path.join(VIDEO_DIR, directory, 'temp')):
                break
            camera_names = set([extract_name(file) for file in files])
            for name in camera_names:
                named_clips = [file for file in files if extract_name(file) == name]
                while named_clips:
                    files_to_merge = [named_clips.pop(0)]
                    while named_clips:
                        if (extract_datetime(named_clips[0]) - (
                                extract_datetime(files_to_merge[-1]) + get_duration(files_to_merge[-1]))) < timedelta(
                                minutes=10):
                            files_to_merge.append(named_clips.pop(0))
                        else:
                            break
                    merge_clips(files_to_merge, os.path.join(VIDEO_DIR, directory, 'temp'),
                                os.path.join(VIDEO_DIR, directory))

        delete_old_files(VIDEO_DIR, timedelta(days=60))

    except Exception as error:
        print(error)

    sleep(100000)
