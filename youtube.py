import pafy
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def query(searchString):
	'''
	Params: searchString - To query youtube
	Return: Dictionary of keys as video titles and values as urls to videos
	'''
	query = urllib.parse.quote(searchString)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)

	urls = {}
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		urls[vid['title']] = 'https://www.youtube.com' + vid['href']
	return urls

query('Dillon Francis - Get Low')
def get_audio(url):
	video = pafy.new(url)
	duration = video.duration
	title = video.title
	bestaudio = video.getbestaudio(preftype="m4a")

	bestaudio.download()

