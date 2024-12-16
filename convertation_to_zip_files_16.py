import zipfile
import os


def archive_folder(zip_name, folder_path):
    # Создаём новый ZIP-архив с именем zip_name
    # Параметр 'w' означает, что мы создаём архив с нуля, ZIP_DEFLATED для сжатия
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Используем os.walk для рекурсивного обхода всех файлов и папок внутри folder_path
        for root, dirs, files in os.walk(folder_path):
            # Проходимся по всем файлам в текущей деректории
            for file in files:
                # Получаем путь к файлу
                file_path = os.path.join(root, file)
                # Добавляем файл в архив, сохраняя относительный путь от корневой папки
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
                # Выводим сообщение о том, что файл был добавлен
                print(f'Файл {file_path} был успешно добавлен в архив.')


# Пример использования
folder_to_archive = 'my_folder' # Указываем папку, которую хотим архивировать
archive_name = "new_archive.zip" # Указываем имя для создаваемого архива

# Вызываем функцию архивации папки
archive_folder(archive_name, folder_to_archive)