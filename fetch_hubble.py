import requests
from get_image import get_img,directory


def get_response(url):
    response = requests.get(url)
    data = response.json()
    return data


def get_img_id(data):
    images_id = [item['id'] for item in data]
    return images_id


def get_img_url(data):
    images_urls = [item['file_url'] for item in data['image_files']]
    return images_urls[1]


def main():
    img_collections = ['wallpaper', 'spacecraft']
    max_img_limit = 6

    for collection_name in img_collections:
        url = 'http://hubblesite.org/api/v3/images/{}?page=all'.format(collection_name)
        if collection_name is 'wallpaper':
            images_id_wal = get_img_id(get_response(url))
        else:
            images_id_spa = get_img_id(get_response(url))
            images_id = images_id_wal + images_id_spa

    for index, image_id in enumerate(images_id, start=1):
        url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
        image_url = get_img_url(get_response(url))
        if index is max_img_limit:
            break
        else:
            path = '{}/hubble/{}.jpg'.format(directory,index)
            get_img(image_url, path)


if __name__ == "__main__":
    main()


    
