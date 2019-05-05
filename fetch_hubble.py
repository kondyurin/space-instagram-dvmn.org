import os
import requests
from get_image import fetch_img, get_file_extension


def fetch_json(url, payload):
    response = requests.get(url,params=payload)
    data = response.json()
    return data


def fetch_hubble_photos():
    """Fetch photo from 'wallpaper' hubble collection"""
    img_collection = 'wallpaper'
    images_ids = []
    payload = {
        'page': 'all'
    }
    url = 'http://hubblesite.org/api/v3/images/{}'.format(img_collection)
    for item in fetch_json(url,payload):
        images_ids.append(item['id'])
    for index, image_id in enumerate(images_ids, start=1):
        payload = {}
        url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
        data = fetch_json(url, payload)
        path = os.path.join('images', '{}'.format(index))
        for image_data in data['image_files']:
            img_extension = get_file_extension(image_data['file_url'])
            fetch_img(image_data['file_url'], '{}{}'.format(path, img_extension))
            break  # break to save only first photo size

if __name__ == "__main__":
    fetch_hubble_photos()
