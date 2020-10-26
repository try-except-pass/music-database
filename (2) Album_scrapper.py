import requests
from bs4 import BeautifulSoup as bs
import pickle
from time import sleep
import os.path

with open('My Artists_Albums.pickle', "rb") as file:
    data = pickle.load(file)

band_discography = {}
band_discography_low_case = {}
band_singles = {}
band_singles_low_case = {}

for artist in data:
    sleep(1)
    wiki_template = requests.get("https://www.discogs.com/artist/" + artist)
    page_soup  = bs(wiki_template.text, "html.parser")
    discography = page_soup.find(id="artist").find_all(class_ = "title")

    albums = []
    albums_low_case = []

    singles = []
    singles_low_case = []

    for i in discography:
        try:
            x = i.find(class_ = "format").get_text()
            if x.find("Album")>=1 or x.find("EP")>=1:
                Y = i.find("a").get_text()
                y = ''.join(e.lower() for e in Y if e.isalnum())
                if y not in albums_low_case:
                    albums.append(Y)
                    albums_low_case.append(y)
            elif x.find("Single")>=1:
                Y = i.find("a").get_text()
                y = ''.join(e.lower() for e in Y if e.isalnum())
                if any(a.startswith(y) for a in singles_low_case) or any(a.startswith(y) for a in albums_low_case):
                    pass
                else:
                    singles.append(Y)
                    singles_low_case.append(y)    
        except:
            pass
    
    band_discography["%s" % artist] = albums
    band_discography_low_case["%s" % (''.join(e.lower() for e in artist if e.isalnum()))] = albums_low_case
    band_singles["%s" % artist] = singles
    band_singles_low_case["%s" % (''.join(e.lower() for e in artist if e.isalnum()))] = singles_low_case

with open("Band Discography.pickle", "ab") as file:
    pickle.dump(band_discography, file)
    print(f"Discography Done")

with open("Band Discography_low_case.pickle", "ab") as file:
    pickle.dump(band_discography_low_case, file)
    print(f"Discography_low_case Done")

with open("Band Singles.pickle", "ab") as file:
    pickle.dump(band_singles, file)
    print(f"Singles Done")

with open("Band Singles_low_case.pickle", "ab") as file:
    pickle.dump(band_singles_low_case, file)
    print(f"Singles_low_case Done")

