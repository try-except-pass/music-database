import pickle
import os.path

save_path = input("Where's the discography registry files? ")
data_file_directory = os.path.join(save_path, '')
with open (data_file_directory + "Band Discography.pickle", "rb") as file:
    band_discography = pickle.load(file)
with open (data_file_directory + "Band Discography_low_case.pickle", "rb") as file:
    band_discography_low_case = pickle.load(file)
with open (data_file_directory + "Band Singles.pickle", "rb") as file:
    band_singles = pickle.load(file)
with open (data_file_directory + "Band Singles_low_case.pickle", "rb") as file:
    band_singles_low_case = pickle.load(file)
with open (data_file_directory + "My Artists_Albums.pickle", "rb") as file:
    my_artists_albums = pickle.load(file)

my_artists_albums_low_case = {}

for artist in my_artists_albums:
    albums = my_artists_albums[artist]
    my_album_low_case = []
    for album in albums:
        my_album_low_case.append("".join(e.lower() for e in album if e.isalnum()))
    my_artists_albums_low_case[artist] = my_album_low_case    
    
for artist in my_artists_albums_low_case:
    for album in my_artists_albums_low_case[artist]:
        try:
            x = band_discography_low_case[artist].index(album)
            band_discography[artist].pop(x)
        except:
            pass
        try:
            x = band_singles_low_case[artist].index(album)
            band_singles[artist].pop(x)
        except:
            pass        

save_path = input("Where do you want to save file? ")
file_directory = os.path.join(save_path, "Albums-singles Missing by artist.txt")

with open(file_directory, "a") as file:
    for i in band_discography:
        x = str(band_discography[i])
        try:
            z = str(band_singles[i])
            file.write( i + "\nAlbums - " + x + "\nSingles - " + z + "\n\n") 
        except:
            file.write( i + "\nAlbums - " + x + "\n\n") 
        
    print("Done")