from time import sleep
from pytube import YouTube
from pytube.cli import on_progress
from DownloadSubtitle import getSubtitle
from DownloadVideo import getVideo
import unicodedata
import re
import os

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value)
    return re.sub(r'[-\s]+', ' ', value)

def downloadLink(link): 
    yt = YouTube(link, on_progress_callback=on_progress) 
    title = slugify(yt.title)
    print('Downloading ' + title)
    getVideo(yt, title)
    print()
    getSubtitle(link[link.index('v=') + 2 :], title)

cwd = os.getcwd()
links=open('links_file.txt','r') 
for link in links:
    downloadLink(link)


