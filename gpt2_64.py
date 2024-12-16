# Установка библиотеки.
# pip install Pillow.

from PIL import Image

def convert_to_black_and_white(input_image_path, output_image_path):
    # Открывае изображение.
    image = Image.open(input_image_path)

    # Преобразуем изображение в чёрное-белое.
    bw_image = image.convert("L")

    # Сохраняем чёрно-белое изображение.
    bw_image.save(output_image_path)
    print(f"Готово! Данный экземпляр был сохранён под названием: {output_image_path}")

# Пример использования.
input_path = input("Молодой человек, пожалуйста введите путь к оригинальному типу изображения (цветное изображение...): ")
output_path = input("Введите путь к папке для сохранения чёрно-белого изображения: ")
convert_to_black_and_white(input_path, output_path)
