import requests
from get_image import fetch_img,directory


def main():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    launch_data = response.json()

    for index, img in enumerate(launch_data['links']['flickr_images'], start=1):
        path = os.path.join(directory,index)
        fetch_img(img,path)


if __name__ == "__main__":
    main()