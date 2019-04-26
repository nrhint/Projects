##Nathan Hinton

#Learning from:
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

#Goal is to build a scraper that will look on news sites for a name or event.

links = ['http://abcnews.go.com/', 'http://www.cnn.com/', 'http://www.nbcnews.com/',
         'http://www.huffingtonpost.com/']

#Try to look through these sites for a name/event.

import urllib2
from BeautifulSoup import BeautifulSoup
