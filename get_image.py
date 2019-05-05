import os
import requests
import shutil


def fetch_img(url, path):
    """Save image in folder"""
    if not os.path.exists('images'):
        os.makedirs('images')
    response = requests.get(url, stream=True)
    if not response.ok:
        return None
    with open(path, 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)


def get_file_extension(url):
    """Return file extension"""
    file_extension = ''.join(('.', url.split('.')[-1:][0]))
    return file_extension


if __name__ == '__main__':
    img_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    fetch_img(img_url, 'images/img1{}'.format(get_file_extension(img_url)))