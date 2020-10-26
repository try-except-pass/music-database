import pickle
import os.path

with open ("My Artists_Albums.pickle", "rb") as file:
    my_artists_albums = pickle.load(file)
with open ("Band Discography.pickle", "rb") as file:
    band_discography = pickle.load(file)
with open ("Band Discography_low_case.pickle", "rb") as file:
    band_discography_low_case = pickle.load(file)
with open ("Band Singles.pickle", "rb") as file:
    band_singles = pickle.load(file)
with open ("Band Singles_low_case.pickle", "rb") as file:
    band_singles_low_case = pickle.load(file)

for artist in my_artists_albums:
    artist_low = ''.join(e.lower() for e in artist if e.isalnum())
    for album in my_artists_albums[artist]:
        album_low = ''.join(e.lower() for e in album if e.isalnum())
        try:
            x = band_discography_low_case[artist_low].index(album_low)
            band_discography[artist].pop(x)   
        except:
            pass
        try:
            x = band_singles_low_case[artist_low].index(album_low)
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