#import soundcloud     
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from youtube import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os

'''
Read your likes on soundcloud and search youtube.

Currently unable to use soundcloud API until they open registration for apps again.

'''

#driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
#driver.get("https://soundcloud.com/limitlessnight/show-me")


url = "https://soundcloud.com/sethybrunes/likes"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

collection = soup.findAll('article')

# Create list of songs
songList = []
for article in collection[1:]:
	song = article.find('a')
	if "-" in song.text:
		songList.append(song.text)
	else:
		author = song['href'].split('/')[1]
		author = author.replace("_", " ")
		songList.append(author + ' - ' + song.text)

file_names = [file.split(".")[0] for file in os.listdir()]

for song in songList:
	youtube_songs = query(song)
	bestMatch = process.extractOne(song, youtube_songs.keys(), score_cutoff=90)
	print("{} - {}".format(song, bestMatch))
	if bestMatch[0] not in file_names:
		get_audio(youtube_songs[bestMatch[0]])
	else:
		print("Song {} already in directory".format(bestMatch[0]))