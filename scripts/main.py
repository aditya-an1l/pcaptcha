import time
import rich
from captcha.image import ImageCaptcha
from PIL import Image

import string
import random


def generate_text_captcha(character_length):
    text = "".join(
        random.choices(string.ascii_letters + string.digits, k=character_length)
    )
    return text


def generate_captcha(character_length=7, save_path="./media/captcha.png"):
    captcha_image = ImageCaptcha(width=500, height=100)
    captcha_text = generate_text_captcha(character_length)

    data = captcha_image.generate(captcha_text)

    captcha_image.write(captcha_text, save_path)
    return captcha_text


if __name__ == "__main__":
    save_path = "./media/captcha.png"
    text = generate_captcha(7, save_path)
    print("Captcha Text: ", text)
    time.sleep(2)

    Image.open(save_path).show()
