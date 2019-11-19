#!/usr/bin/env python3
import sys,os
import urllib.parse
import requests 
import wget

try:
    url =  sys.argv[1]
except IndexError as identifier:
    print("Enter URL of spotify song")
    exit(0)


url = url.split("?")[0]

url = urllib.parse.quote(url)


PARAMS = {
    'Host':'https://spotify-downloader.ml',
    'q':url,
          }
os.system('clear')


r = requests.post(url = 'https://spotify-downloader.ml/index.php', data = PARAMS)



downloadpage = r.text 


ind = downloadpage.find('/music/')



indlast  = downloadpage.find('.mp3',ind)

if(ind == -1 or indlast == -1):

    print("The given link is must be of valid song (Playlist's are not downloadable)")
    exit()

downloadlink =   downloadpage[ind:indlast + 4]

download = 'https://spotify-downloader.ml/' + downloadlink

print(download)

filename = os.path.basename(download)

directory = os.getcwd()
try:
    wget.download(download, directory + '/' + filename)    
finally:
    print("Fail to download")
