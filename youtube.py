import pafy

def get_audio(url):
	video = pafy.new(url)
	duration = video.duration
	title = video.title
	bestaudio = video.getbestaudio(preftype="m4a")

	bestaudio.download()

get_audio("https://www.youtube.com/watch?v=uUh2IaBW-zQ")