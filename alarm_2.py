import time
from datetime import datetime
import pygame

def play_music(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1) # Воспроизведение в цикле

def stop_music():
    pygame.mixer.music.stop()

def set_alarm(alarm_time, music_file):
    print(f"Вы успешно установили будильник на время: {alarm_time}.")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Здравствуйте. Вам пора просыпаться, время сна вышло!")
            play_music(music_file)
            break
        time.sleep(30) # Проверка каждые 30 секунд

if __name__ == "__main__":
    alarm_time = input("Впишите время, на которое хотите включить будильник ( пишите в формате ЧЧ:ММ ): ")
    music_file = input("Хотели-бы поставить рингтон? Это очень просто сделать, укажить путь к файлу, где хранится музыка: ")
    set_alarm(alarm_time, music_file)

    # Ожидаем 10 минут перед остановкой музыки (можно изменить)
    time.sleep(600)
    stop_music()
