import requests
from get_image import fetch_img,directory


def fetch_json(url,payload):
    response = requests.get(url,params=payload)
    data = response.json()
    return data


def main():
    img_collections = ['wallpaper', 'spacecraft']
    max_img_limit = 6
    images_id_wal = []
    images_id_spa = []
    images_urls = []

    for collection_name in img_collections:
        payload = {
            'page': 'all'
        }
        url = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
        for item in fetch_json(url,payload):
            if collection_name is 'wallpaper':
                images_id_wal.append(item['id'])
            else:
                images_id_spa.append(item['id'])
                images_id = images_id_wal + images_id_spa

    for index, image_id in enumerate(images_id, start=1):
        payload = {}
        url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
        for item in fetch_json(url,payload)['image_files']:
            images_urls.append(item['file_url'])
        if index is max_img_limit:
            break
        else:
            path = '{}/hubble/{}.jpg'.format(directory,index)
            for img_url in images_urls:
                fetch_img(img_url, path)


if __name__ == "__main__":
    main()


    
