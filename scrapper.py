import requests
from bs4 import BeautifulSoup

dateSearch = input("Enter date you wish to search in format yyyy-mm-dd: ")
typeSearch = input("Enter S for song and A for Album: ")
findTrack = input("Album or Song name: ")

if typeSearch.lower()=='s':
    req=requests.get("https://www.billboard.com/charts/hot-100/{}".format(dateSearch))
elif typeSearch.lower()=='a':
    req=requests.get("https://www.billboard.com/charts/billboard-200/{}".format(dateSearch))
else:
    exit()


soup = BeautifulSoup(req.content,"html.parser")
tracks = soup.find_all("span", class_="chart-element__information")

songs=[]
artists=[]
found=False

for track in tracks:
    songs.append(track.find("span",class_="chart-element__information__song text--truncate color--primary").text)
    artists.append(track.find("span", class_="chart-element__information__artist text--truncate color--secondary").text)

for index in range(len(songs)):
    if songs[index].lower() == findTrack.lower():
        position = index+1
        print(f'Position is #{position}')
        found=True

if found == False:
    print("Not on Charts")