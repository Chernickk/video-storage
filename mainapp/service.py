import os
import subprocess
from datetime import datetime, timedelta
from uuid import uuid4

from django.conf import settings
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

from .models import Record


def create_new_filename(filename):
    return f'{str(uuid4())[:8]}{filename.split(":")[-1][:-4]}.avi'


def get_subclip(record, start_time, end_time):
    filename = record.file_name
    datetime_formatted = datetime.strptime(filename[:19], '%Y-%m-%d_%H:%M:%S')
    output_filename = create_new_filename(filename)

    if isinstance(start_time, datetime):
        start_offset = start_time - datetime_formatted
        start_offset = start_offset.total_seconds()
    else:
        start_offset = start_time

    if isinstance(end_time, datetime):
        end_offset = end_time - datetime_formatted
        end_offset = end_offset.total_seconds()
    else:
        end_offset = end_time

    if not os.path.exists(settings.TEMP_MEDIA_FOLDER):
        os.mkdir(settings.TEMP_MEDIA_FOLDER)

    ffmpeg_extract_subclip(
        filename=f'media/{filename}',
        t1=start_offset,
        t2=end_offset,
        targetname=os.path.join(settings.TEMP_MEDIA_FOLDER, output_filename)
    )

    return output_filename


def make_clip_from_two_subclips(record1, record2, start_time, end_time):
    end_of_record1 = VideoFileClip(f'media/{record1.file_name}').duration

    file1 = get_subclip(record1, start_time=start_time, end_time=end_of_record1)
    file2 = get_subclip(record2, start_time=0, end_time=end_time)

    output_filename = create_new_filename(record1.file_name)

    subprocess.call(['mkvmerge',
                     '-o',
                     f'{os.path.join(settings.TEMP_MEDIA_FOLDER, output_filename)}',
                     f'{file1}',
                     '+',
                     f'{file2}'])

    os.remove(file1)
    os.remove(file2)

    return output_filename


def get_output_file(start_time: datetime, end_time: datetime, car_id):
    car_id = int(car_id)

    recs = Record.objects.filter(start_time__lte=start_time, end_time__gte=start_time, car__id=car_id)
    recs2 = Record.objects.filter(start_time__lte=end_time, end_time__gte=end_time, car__id=car_id)

    files = []

    if set(recs) != set(recs2) and len(recs) == len(recs2):
        for i in range(len(recs)):
            file = make_clip_from_two_subclips(recs[i], recs2[i], start_time=start_time, end_time=end_time)
            files.append(file)
    else:
        for rec in recs:
            file = get_subclip(rec, start_time=start_time, end_time=end_time)
            files.append(file)

    return files
