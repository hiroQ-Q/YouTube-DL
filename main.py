#import list
from yt_dlp import YoutubeDL
import urllib.request, urllib.error
import sys
import os
import ctypes
import time


#搭載予定だったもの(過去形)
def update_title():
    while True:
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - start))
        ctypes.windll.kernel32.SetConsoleTitleW(f'Time elapsed: {elapsed}')
        time.sleep(0.4)

#URL読み込み
def URL():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'YouTube Download-Tool-v1.0')
    print("Please enter YouTube URL")
    global URL
    URL = input("URL | ")
    #print(URL)

#URLを確認
def checkURL(url):
    if 'youtube.com/watch?v=' in url:
        try:
            f = urllib.request.urlopen(url)
            print ("OK : " + url )
            f.close()
        except:
            print ("NotFound : " + url)
            sys.exit(0)
    elif 'youtu.be/' in url:
        try:
            f = urllib.request.urlopen(url)
            print ("OK : " + url )
            f.close()
        except:
            print ("NotFound : " + url)
            sys.exit(0)
    elif 'youtube.com/playlist?' in url:
        try:
            f = urllib.request.urlopen(url)
            print ("OK : " + url )
            f.close()
        except:
            print ("NotFound : " + url)
            sys.exit(0)
    elif 'youtube.com/channel' in url:
        try:
            f = urllib.request.urlopen(url)
            print ("OK : " + url )
            f.close()
        except:
            print ("NotFound : " + url)
            sys.exit(0)
    else:
        print ("Please put the URL of YouTube : " + url )
        sys.exit(0)

#download
def download(url):
    ctypes.windll.kernel32.SetConsoleTitleW(f'YouTube Download-Tool-v1.0 | URL : {url}')
    #print(url)
    ydl_opts = {
        'format': 'mp4',
    }
    #m4a ffmpeg required
    with YoutubeDL(ydl_opts) as ydl:
        os.system('cls')
        ydl.download([url])

#起動
if __name__ == "__main__": 
    URL()
    checkURL(URL)
    download(URL)
    #start = time.time()
    #update_title()