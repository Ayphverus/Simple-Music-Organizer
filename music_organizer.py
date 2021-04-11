#!/usr/bin/python3

from tinytag import TinyTag
import os
import os.path
import shutil

print("Current Directory: " + os.getcwd())

PATH = os.getcwd() + '/Music'
OUT_PATH = os.getcwd() + '/MP3'
conditions = {"/": "",
              "\\": "",
              "?": "",
              "<": "",
              ">": "",
              "*": "",
              ":": "",
              "\"": "",
              "|": ""}

if (os.path.isdir(PATH)) is False:
    print("Cannot find \"Music Folder\" in current directory.")
    exit(0)

if (os.path.isdir(OUT_PATH)) is False:
    os.mkdir(OUT_PATH)
else:
    print("Please Manually Remove Folder At: " + OUT_PATH)
    exit(0)


def filter_file_string(text):
    for key in conditions:
        text = text.replace(key, conditions[key])
    text = text.rstrip()
    return text


for root, subFolder, files in os.walk(PATH):
    for item in files:
        if item.endswith(".mp3") or item.endswith(".flac"):
            fileNamePath = str(os.path.join(root, item))
            #print(fileNamePath)

            tag = TinyTag.get(fileNamePath)
            album = 'None'
            artist = 'Various Artists'

            if tag.album is not None:
                album = tag.album
            elif tag.title is not None:
                album = tag.title
            else:
                album = item
                album = album.split('.')[0]

            if tag.albumartist is not None:
                artist = tag.albumartist
            elif tag.artist is not None:
                artist = tag.artist

            artist = filter_file_string(artist)
            album = filter_file_string(album)
            artist_path = str(os.path.join(OUT_PATH, artist)).replace("\\", "/")
            if (os.path.isdir(artist_path)) is False:
                os.mkdir(artist_path)
            album_path = str(os.path.join(artist_path, album)).replace("\\", "/")
            if (os.path.isdir(album_path)) is False:
                os.mkdir(album_path)
            file_destination = str(os.path.join(album_path, item)).replace("\\", "/")
            print(file_destination)
            shutil.copy2(fileNamePath, file_destination)

print("Done")


