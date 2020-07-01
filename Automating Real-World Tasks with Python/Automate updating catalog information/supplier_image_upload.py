#!/usr/bin/env python3
import os

import requests

url = "http://localhost/upload/"
image_location = os.path.join(os.getcwd(), "supplier-data/images")
files = os.listdir(image_location)

for f in files:
	full_path = os.path.join(image_location, f)
	if f.endswith(".jpeg"):
		with open(full_path, 'rb') as opened:
			r = requests.post(url, files={'file': opened})