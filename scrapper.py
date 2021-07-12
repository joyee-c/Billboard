import requests
from bs4 import BeautifulSoup
#user input to gate date and type of search
dateSearch = input("Enter date you wish to search in format yyyy-mm-dd: ")
contentSearch = input("Enter P to search for position or N to search by name: ")
typeSearch = input("Enter S for song and A for Album: ")
if contentSearch.lower()=='n':
    findTrack = input("Album or Song name: ")
else:
    number = input("Enter position number: ")
    number = int(number)

    #chart which will be scrapped depending on user input
if typeSearch.lower()=='s':
    req=requests.get("https://www.billboard.com/charts/hot-100/{}".format(dateSearch))
elif typeSearch.lower()=='a':
    req=requests.get("https://www.billboard.com/charts/billboard-200/{}".format(dateSearch))
else:
    exit()

#scrapping chart
soup = BeautifulSoup(req.content,"html.parser")
tracks = soup.find_all("span", class_="chart-element__information")

songs=[]
artists=[]
found=False

#get songs and artists names from the content
for track in tracks:
    songs.append(track.find("span",class_="chart-element__information__song text--truncate color--primary").text)
    artists.append(track.find("span", class_="chart-element__information__artist text--truncate color--secondary").text)
  
#return user request either the chart position of a desired song or album or an album or song in a specific position
if contentSearch.lower()=='p':
    print(f'{artists[number]} - {songs[number]}')
else:
    for index in range(len(songs)):
        if songs[index].lower() == findTrack.lower():
            position = index+1
            print(f'Position is #{position}')
            found=True

    if found == False:
        print("Not on Charts")
