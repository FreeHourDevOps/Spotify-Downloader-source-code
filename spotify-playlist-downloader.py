#!/usr/bin/env python3
import sys,os
import urllib.parse
import requests 
import wget
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading



def downloadsong(url):
    PARAMS = {
        'Host':'https://spotify-downloader.ml',
        'q':url,
            }
    


    r = requests.post(url = 'https://spotify-downloader.ml/index.php', data = PARAMS)



    downloadpage = r.text 


    ind = downloadpage.find('/music/')



    indlast  = downloadpage.find('.mp3',ind)

    if(ind == -1 or indlast == -1):

        print("Some Songs from Playlist are now downloadable")
        exit()

    downloadlink =   downloadpage[ind:indlast + 4]

    download = 'https://spotify-downloader.ml/' + downloadlink

    

    filename = os.path.basename(download)
    print('\n'+filename)
    directory = os.getcwd()
    try:
        wget.download(download, directory + '/' + filename)    
    finally:
        print()
    print('\n successfully downloaded: '+filename)



os.system('clear')



try:
    purl =  sys.argv[1]
except IndexError as identifier:
    print("Enter URL of spotify Playlist")
    exit(0)



html = urlopen(purl) # Insert your URL to extract
bsObj = BeautifulSoup(html.read(),features="lxml")
data = list()
for link in bsObj.find_all('meta'):
    data.append(str(link.get('content')))



songs = list()
common = 'https://open.spotify.com/track/'
for link in data:
    if(link.find(common)!= -1):
        songs.append(link)

print("\n Wait a sec,we generating download links for you")
for url in songs:
    thread = threading.Thread(target=downloadsong, args=(url,))
    thread.start()

