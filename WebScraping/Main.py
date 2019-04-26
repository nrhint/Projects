##Nathan Hinton

#Learning from:
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

#Goal is to build a scraper that will look on news sites for a name or event.

links = ['http://abcnews.go.com/', 'http://www.cnn.com/', 'http://www.nbcnews.com/',
         'http://www.huffingtonpost.com/']

#Try to look through these sites for a name/event.

from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re

webpage = urlopen('https://www.pythonforbeginners.com/python-on-the-web/scraping-websites-with-beautifulsoup/').read()

soup2 = BeautifulSoup(webpage)

#print soup2.findAll("title")

titleSoup = soup2.findAll("title")

linkSoup = soup2.findAll("link")
#Cycle through the links:
for site in links:
    page = urlopen(str(site))
