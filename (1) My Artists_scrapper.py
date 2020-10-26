from mutagen.easyid3 import EasyID3 as prop
import os
import pickle

music_folder = input("Where's your music? ")
all_files = [os.path.join(root, name)
             for root, dirs, files in os.walk(music_folder)
             for name in files
             if name.endswith((".mp3")) or name.endswith((".flac"))]

full_list = {}
for file in all_files:
    properties = prop(file)
    artist = "".join(properties.pop("artist"))
    album = "".join(properties.pop("album"))
    if artist not in full_list:
        full_list[artist] = [] 
        if album not in full_list[artist]:
            full_list[artist].append(album)

save_path = input("Where do you want to save file? ")
file_directory = os.path.join(save_path, 'My Artists_Albums.pickle')

with open(file_directory, "ab") as file:
    pickle.dump(full_list, file)
    print("Done")