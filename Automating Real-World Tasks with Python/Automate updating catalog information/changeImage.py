#!/usr/bin/env python3

from PIL import Image
from PIL import UnidentifiedImageError
import os

path = os.path.join(os.getcwd(),"supplier-data/images")


for file in os.listdir(path):
    file_path = os.path.join(path, file)
    try:
        im = Image.open(file_path)
        newim = im.convert('RGB').rotate(90).resize((600,400))
        newim.save(file_path.replace(".tiff",".jpeg"), quality=95)
    except UnidentifiedImageError:
        continue