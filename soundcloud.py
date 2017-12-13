#import soundcloud     
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
Read your likes on soundcloud and search youtube.

Currently unable to use soundcloud API until they open registration for apps again.

'''

driver = webdriver.Firefox()
url = "https://soundcloud.com/you/likes"
req = driver.get(url)
soup = BeautifulSoup(req.content, "html.parser")
print(soup.prettify())
collection = soup.findAll('div', {'class': 'collectionSection'})
print(collection)