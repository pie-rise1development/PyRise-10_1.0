import psutil
import pygetwindow
import time

while True:

    windows = pygetwindow.getAllTitles()

    for window in windows:
        if 'Браузер' in window and 'Новости' in window:
            procs = psutil.process_iter(['pid', 'name'])
            for proc in procs:
                if proc.info['name'] == 'browser.exe':
                    proc.kill()


    time.sleep(1)