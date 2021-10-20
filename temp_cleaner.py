import os
import time
import schedule

TEMP_MEDIA_FOLDER = 'media/temp'


def job():
    for file in os.listdir(TEMP_MEDIA_FOLDER):
        os.remove(os.path.join(TEMP_MEDIA_FOLDER, file))
    print('temp video removed')  # logger


schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
