import os
import requests
import shutil


directory = 'images'


def fetch_img(url, path):
    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(url, stream=True)
    if not response.ok:
        return
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


