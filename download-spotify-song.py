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
    'Host':'spotify-downloader.ml',
    'q':url,
          }

r = requests.post(url = 'http://spotify-downloader.ml/index.php', data = PARAMS)

downloadpage = r.text 


ind = downloadpage.find('/music/')

indlast  = downloadpage.find('.mp3',ind)

downloadlink =   downloadpage[ind:indlast + 4]

download = 'http://spotify-downloader.ml' + downloadlink



filename = os.path.basename(download)

directory = os.getcwd()

wget.download(download, directory + '/' + filename)

