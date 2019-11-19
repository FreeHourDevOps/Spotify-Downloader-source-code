#!/usr/bin/env python3
import sys,os
import urllib.parse
import requests 
import wget
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
from termcolor import colored, cprint 
import time

selector = ""


complete_downloaded_song_list = list()




threadcount = 0


def pdown():
    pass


def download_playlist():
    global threadcount
    url = input("Enter URL of spotify song(e.g https://open.spotify.com/album/3Z6f):")
    if True :#url.find("open.spotify.com/album") != -1:
        print("inside Album")
        html = urlopen(url) # Insert your URL to extract
        bsObj = BeautifulSoup(html.read(),features="lxml")
        data = list()
        for link in bsObj.find_all('meta'):
            data.append(str(link.get('content')))

        songs = list()
        common = 'https://open.spotify.com/track/'
        for link in data:
            if(link.find(common)!= -1):
                songs.append(link)
        threadl = list()
        if songs.__len__() > 10:
            cho = int(input("More than 10 songs in playlist \n 1.Download All at a time \n 2.Split Download into 10 at a time(recomanded)\n Enter Your Choice:"))
            if cho == 1: 
                print("\n Wait a sec,we generating download links for you")
                for url in songs:
                    thread = threading.Thread(target=downloadsong, args=(url,))
                    threadl.append(thread)
                    thread.start()
                
                for thr in threadl:
                    thr.join()

            if cho == 2:
                print("\n Wait a sec,we generating download links for you")
                while (songs.__len__() != 0):
                    if (threadcount <= 10):
                        thread = threading.Thread(target=downloadsong, args=(songs[0],))
                        threadl.append(thread)
                        thread.start()
                        songs.pop(0)
                        threadcount = threadcount + 1
                    else:
                        time.sleep(5)
                    
                while threadcount != 0:
                    time.sleep(10)
        else:
            print("\n Wait a sec,we generating download links for you")
            for url in songs:
                thread = threading.Thread(target=downloadsong, args=(url,))
                threadl.append(thread)
                thread.start()
            
            for thr in threadl:
                thr.join()

    elif url.find("open.spotify.com/playlist") != -1:
        html = urlopen(url) # Insert your URL to extract
        bsObj = BeautifulSoup(html.read(),features="lxml")
        data = list()
        for link in bsObj.find_all('meta'):
            data.append(str(link.get('content')))

        songs = list()
        common = 'https://open.spotify.com/track/'
        for link in data:
            if(link.find(common)!= -1):
                songs.append(link)
        threadl = list()
        if songs.__len__() > 10:
            cho = int(input("More than 10 songs in playlist \n 1.Download All at a time \n 2.Split Download into 10 at a time(recomanded)\n Enter Your Choice:"))
            if cho == 1: 
                print("\n Wait a sec,we generating download links for you")
                for url in songs:
                    thread = threading.Thread(target=downloadsong, args=(url,))
                    threadl.append(thread)
                    thread.start()
                
                for thr in threadl:
                    thr.join()

            if cho == 2:
                print("\n Wait a sec,we generating download links for you")
                while (songs.__len__() != 0):
                    if (threadcount <= 10):
                        thread = threading.Thread(target=downloadsong, args=(songs[0],))
                        threadl.append(thread)
                        thread.start()
                        songs.pop(0)
                        threadcount = threadcount + 1
                    else:
                        time.sleep(5)
                    
                while threadcount != 0:
                    time.sleep(10)
    else:
        print("Given Link Is Invalid")





def downloadsong(url):
    global threadcount
    PARAMS = {
        'Host':'https://spotify-downloader.ml',
        'q':url,
            }
    


    r = requests.post(url = 'https://spotify-downloader.ml/index.php', data = PARAMS)



    downloadpage = r.text 


    ind = downloadpage.find('/music/')



    indlast  = downloadpage.find('.mp3',ind)

    if(ind == -1 or indlast == -1):

        print("Some Songs from this Playlist are not downloadable")
    else:

        downloadlink =   downloadpage[ind:indlast + 4]

        download = 'https://spotify-downloader.ml/' + downloadlink

        

        filename = os.path.basename(download)
        print('\n'+filename)
        directory = os.getcwd()
        try:
            wget.download(download, directory + '/' + filename)    
            complete_downloaded_song_list.append(filename)
        finally:
            print()
        print('\n successfully downloaded: '+filename)
    threadcount = threadcount - 1



def download_song():
    url =   input("Enter URL of spotify song(e.g https://open.spotify.com/track/0CqfDR):")
    if url.find("open.spotify.com/track") != -1:
        url = url.split("?")[0]

        url = urllib.parse.quote(url)


        PARAMS = {
            'Host':'https://spotify-downloader.ml',
            'q':url,
                }
        r = requests.post(url = 'https://spotify-downloader.ml/index.php', data = PARAMS)
        downloadpage = r.text 

        ind = downloadpage.find('/music/')

        indlast  = downloadpage.find('.mp3',ind)

        if(ind == -1 or indlast == -1):

            print("The given link is must be of valid song")

        downloadlink =   downloadpage[ind:indlast + 4]

        download = 'https://spotify-downloader.ml/' + downloadlink

        print(download)

        filename = os.path.basename(download)
        directory = os.getcwd()
        try:
            wget.download(download, directory + '/' + filename)   
            complete_downloaded_song_list.append(filename) 
        finally:
            print("Fail to download")
    else:
        print("Given link is invalid")





def endeverything():
    if complete_downloaded_song_list.__len__() != 0:
        print("Downloaded Song List:")
        for song in complete_downloaded_song_list:
            print(song)
    exit()

def invalid_argument():
    print("invalid Option")


def select_option(i):
    switcher={
            1:download_song,
            2:download_playlist,
            3:endeverything,
            }
    func=switcher.get(i,invalid_argument)
    return func()


while selector != 3:
    #os.system('clear')


    cprint(r"""
Developed BY
                       /\             /\
                      |`\\_,--="=--,_//`|
                      \ ."  :'. .':  ". /
                     ==)  _ :  '  : _  (==
                       |>/O\   _   /O\<|
                       | \-"~` _ `~"-/ |
                      >|`===. \_/ .===`|<
                .-"-.   \==='  |  '===/   .-"-.
.--------------{'. '`}---\,  .-'-.  ,/---{.'. '}-------------.
 )             `"---"`     `~-===-~`     `"---"`            (
(           __  __        ____  _ _            _             )
 )         |  \/  |_ __  / ___|(_) | ___ _ __ | |_          (
(          | |\/| | '__| \___ \| | |/ _ \ '_ \| __|          )
 )         | |  | | |     ___) | | |  __/ | | | |_          (
(          |_|  |_|_|    |____/|_|_|\___|_| |_|\__|          )
 )                                                          (
'------------------------------------------------------------'

 ""","blue")
    selector = input("1.Download Song\n2.Download Playist\n3.Exit\nEnter your Choice:")
    func = select_option(int(selector))
    func