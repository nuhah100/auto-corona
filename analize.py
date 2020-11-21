from PIL import Image
from pytesseract import *


def run(image_path):
    im = Image.open(image_path)
    text = image_to_string(im)
    return text
