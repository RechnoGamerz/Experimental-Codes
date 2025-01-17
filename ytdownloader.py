from pytube import YouTube
from sys import argv

link = str(input("Pls paste or enter the link:"))
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("R:\Clips")
print("Downloaded: ",yt.title)