import os
import requests
import shutil


directory = 'images'


def get_img(url,path):
    if not os.path.exists(directory):
        os.makedirs(directory)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    print('succesfull!')


