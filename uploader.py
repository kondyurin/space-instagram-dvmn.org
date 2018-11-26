import glob
import os
import sys
import time
from io import open
from instabot import Bot


PASSWORD = os.environ["instagram_pass"]
LOGIN = os.environ["instagram_login"]


def read_txt():
    posted_pic_list = []
    try:
        with open('pics.txt', 'r', encoding='utf8') as f:
            posted_pic_list = f.read().splitlines()
    except Exception:
        posted_pic_list = []
    return posted_pic_list


def write_txt(pic):
    with open('pics.txt', 'a', encoding='utf8') as f:
        f.write(pic + "\n")


def main(posted_pic_list):
    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    pics = glob.glob("**/*.jpg", recursive=True)
    try:
        for pic in pics:
            if pic in posted_pic_list:
                continue
            else:
                posted_pic_list.append(pic)
                write_txt(pic)
                bot.upload_photo(pic)
    except ValueError as e:
        print(str(e))


if __name__ == '__main__':
    main(read_txt())