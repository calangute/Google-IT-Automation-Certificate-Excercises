#!/usr/bin/env python3

import os

from PIL import Image
from PIL import UnidentifiedImageError

image_path = os.path.join(os.getcwd(), "supplier-data/images")

for file in os.listdir(image_path):
    file_path = os.path.join(image_path, file)
    try:
        im = Image.open(file_path)
        new_im = im.convert('RGB').rotate(90).resize((600, 400))
        new_im.save(file_path.replace(".tiff", ".jpeg"), quality=95)
    except UnidentifiedImageError:
        continue
