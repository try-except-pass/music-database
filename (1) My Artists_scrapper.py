from mutagen.easyid3 import EasyID3 as prop
import os
import pickle

music_folder = input("Where's your music? ")
all_files = [os.path.join(root, name)
             for root, dirs, files in os.walk(music_folder)
             for name in files
             if name.endswith((".mp3")) or name.endswith((".flac"))]

full_list = {}
full_list_low_case = {}

for file in all_files:
    properties = prop(file)
    artist = "".join(properties.pop("artist"))
    artist_low = "".join(e.lower() for e in artist if e.isalnum())
    album = "".join(properties.pop("album"))
    album_low = "".join(e.lower() for e in album if e.isalnum())
    if artist_low not in full_list_low_case:
        full_list[artist] = [] 
        full_list_low_case[artist_low] = [] 
        if album_low not in full_list_low_case[artist_low]:
            full_list[artist].append(album)
            full_list_low_case[artist_low].append(album_low)

with open('My Artists_Albums.pickle', "ab") as file:
    pickle.dump(full_list, file)
with open('My Artists_Albums_low_case.pickle', "ab") as file:
    pickle.dump(full_list_low_case, file)

print("Done")