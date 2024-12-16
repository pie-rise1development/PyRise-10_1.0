import pytubefix, pathlib, sys

print("Made by pRiseDev\n-\nЗдравствуйте! Могу предложить вам скачать любое видео по вашему желанию с видео-платформы [YouTube].\n-\nПримечание:\nНе рекомендуется скачивать видео длинной более 60-минут\n-\nВсе логи скачанного видео-ролика будут успешно записаны в отдельный текстовый документ под названием {video_y3t.txt} в той рабочей папки которая будет указана вами в консоли!\n-\nЖелаю вам удачного использования")
print("")
link = input("Пожалуйста, введите ссылку на скачивание видео-ролика: ")
name = input("Введите название, под которым хотите сохранить видео-файл (например, testing.mp4): ")
file = input("Вставьте путь к папке, где должен сохраниться ваш файл (например, C:/User/Your/Computer/path): ")
google = input("Нужно ли вам делать аутентификацию через [Google] аккаунт (Да / Нет): ")

def download_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    print(f"Уровень скачивания: {round(bytes_downloaded, 2)} байтов.")


def downloader(link: str, name: str, file: str, google: str):
    try:
        if google == "Нет":
            yt = pytubefix.YouTube
