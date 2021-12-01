import os
import subprocess
from datetime import timedelta, datetime
from typing import List

import cv2

from settings import DATE_FORMAT, FPS


def extract_datetime(filename):
    return datetime.strptime(filename[:19], DATE_FORMAT)


def extract_name(filename):
    """
    :param filename: str
    :return camera name: str
    """
    return filename.split('.')[0].split('_')[-1]


def get_duration(filename: str) -> timedelta:
    video = cv2.VideoCapture(filename)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = int(frame_count / FPS)

    return timedelta(seconds=duration)


def get_clips_by_name(clips: List[str], name: str):
    camera_clips = [clip for clip in clips if name in clip]
    if camera_clips:
        camera_clips.sort()
        return camera_clips
    return None


def merge_clips(clips: List[str], input_path, out_path: str) -> str:
    """
    Merge clips
    :param out_path: str
    :param clips: list
    :return output merged clip: str
    """
    dt_finish = extract_datetime(clips[-1]) + get_duration(clips[-1])
    camera_name = extract_name(clips[0])
    output_name = f'{datetime.strftime(extract_datetime(clips[0]), DATE_FORMAT)}' \
                  f'__' \
                  f'{datetime.strftime(dt_finish, DATE_FORMAT)}_{camera_name}.mp4'
    output_path = os.path.join(out_path, output_name)

    with open('input.txt', 'w') as f:
        for filename in clips:
            f.write(f"file '{os.path.join(input_path, filename)}'\n")

    subprocess.call(['ffmpeg',
                     '-f', 'concat',
                     '-safe', '0',
                     '-i', 'input.txt',
                     '-c', 'copy',
                     '-y', output_path])

    os.remove('input.txt')

    return output_name
