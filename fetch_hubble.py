import os
import requests
from get_image import fetch_img, get_file_extension


def fetch_json(url, payload):
    response = requests.get(url,params=payload)
    data = response.json()
    return data


def fetch_hubble_photos():
    img_collections = ['wallpaper', 'spacecraft']
    max_img_limit = 3
    images_id_wal = []
    images_id_spa = []
    images_urls = []

    for collection_name in img_collections:
        payload = {
            'page': 'all'
        }
        url = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
        for item in fetch_json(url,payload):
            if not collection_name is 'wallpaper':
                images_id_spa.append(item['id'])
                images_id = images_id_wal + images_id_spa
            images_id_wal.append(item['id'])
                

    for index, image_id in enumerate(images_id, start=1):
        payload = {}
        url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
        for item in fetch_json(url,payload)['image_files']:
            images_urls.append(item['file_url'])
        if index is max_img_limit:
            break
        else:
            path = os.path.join('images', '{}'.format(index))
            for img_url in images_urls:
                img_extension = get_file_extension(img_url)
                fetch_img(img_url, '{}{}'.format(path, img_extension))


if __name__ == "__main__":
    fetch_hubble_photos()


    
