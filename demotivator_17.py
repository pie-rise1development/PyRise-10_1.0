from PIL import Image, ImageDraw, ImageFont, ImageOps

# Загружаем изображение и добавляем рамку
img = Image.open(input("Господин, введите путь к изображению, которое вы хотите превратить в 'МЕМ': ")).resize((780, 600))
bordered_img = ImageOps.expand(img, border=10, fill="white")

# Создаём фон демотиватора и добавляем изображение
demotivator = Image.new("RGB", (800, 750), "black")
demotivator.paste(bordered_img, (0, 0))
draw = ImageDraw.Draw(demotivator)
font_main, font_sub = ImageFont.truetype("arial.ttf", 40), ImageFont.truetype("arial.ttf", 25)

# Добавляем текст
draw.text((235, 620), "Проблемы 'СВО':", font=font_main, fill="white")
draw.text((291, 690), "1. Это ты, еблан!", font=font_sub, fill="white")

demotivator.save("C:/Users/dmitr/Desktop/Test/ai_53.png")