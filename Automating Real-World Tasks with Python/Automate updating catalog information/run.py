#! /usr/bin/env python3

import os

import requests

base_path = os.path.join(os.getcwd(), "supplier/descriptions")
url = "http://localhost/fruits/"


def post_data(fruit_data):
    r = requests.post(url, data=fruit_data)
    r.raise_for_status()


def get_fruits_data(upload=True):
    out = []
    for fi in os.listdir(base_path):
        full_path = os.path.join(base_path, fi)
        if fi.endswith(".txt"):
            with open(full_path, "r") as fp:
                temp = {}
                content = fp.readlines()
                temp["name"] = content[0].strip()
                temp["weight"] = content[1].strip()
                out.append(temp)
                if upload:
                    temp["weight"] = int(temp["weight"].strip("lbs").replace(" ", ""))
                    temp["description"] = "".join(i.strip() for i in content[2:])
                    temp["image"] = fi.replace(".txt", ".jpeg")
                    post_data(temp)
    return out


if __name__ == '__main__':
    get_fruits_data()
