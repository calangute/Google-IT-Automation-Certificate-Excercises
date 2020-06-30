#! /usr/bin/env python3

import os
import requests

base_path = os.path.join(os.getcwd(),"supplier/descriptions")
out = []

for fi in os.listdir(base_path):
	fullpath = os.path.join(base_path, fi)
	if fi.endswith(".txt"):
		with open(fullpath, "r") as fp:
			content = fp.readlines()
			name = content[0].strip()
			weight = int(content[1].strip("lbs\n").replace(" ",""))
			desc = "".join(i.strip() for i in content[2:])
            image = fi.replace(".txt",".jpeg")
			temp = { "name": name, "weight": weight, "description": desc, "image_name": image }
			out.append(temp)
