import os
import requests
import shutil


def fetch_img(url, path):
    if not os.path.exists('images'):
        os.makedirs('images')
    response = requests.get(url, stream=True)
    if not response.ok:
        return None
    with open(path, 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)


if __name__ == '__main__':
    fetch_img('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'images/img1.jpeg')