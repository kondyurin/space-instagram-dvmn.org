import os
import requests
from get_image import fetch_img, get_file_extension


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    launch_data = response.json()

    for index, img in enumerate(launch_data['links']['flickr_images'], start=1):
        img_extension = get_file_extension(img)
        path = os.path.join('images', '{}{}'.format(index, img_extension))
        fetch_img(img, path)


if __name__ == "__main__":
    fetch_spacex_last_launch()