from pytube import Playlist,YouTube
import os
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/playlist?list=PLcqDmjxt30RujZzqIS1sAHz92TZDaRB9d"
# req = requests.get(url)
# soup = BeautifulSoup(req.text,"html.parser")
# title_tags = soup.find_all("span",{"id":"video-title"})

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
titles = []
urls = []
for i, tr in enumerate(soup.select('tr.pl-video')):
    titles.append(tr['data-title'])
    urls.append(tr.a['href'])
print(titles)
print(urls)
# playlist = Playlist(url)
# # #os.exists(~)
# for video in playlist:

#     # if ~~:
#     #     continue
#     # else:
#     YouTube(video).streams.filter(adaptive=True)[0].download()


