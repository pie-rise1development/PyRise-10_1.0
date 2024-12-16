import torch
from diffusers import StableDiffusionPipeline

# Загружаем модель
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cuda")  # Используйте "cpu" если у вас нет GPU

def generate_image(prompt):
    with torch.autocast("cuda"):
        image = pipe(prompt).images[0]
    return image

if __name__ == "__main__":
    user_input = input("Введите запрос для генерации картинки: ")
    image = generate_image(user_input)
    image.save("generated_image.png")
    print("Изображение сохранено как 'generated_image.png'")
