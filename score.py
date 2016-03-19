import re
import os
from bs4 import BeautifulSoup
import urllib.request
import time
while True:
	url=("http://www.espncricinfo.com/ci/engine/match/951341.html")
	page=urllib.request.urlopen(url)
	soup = BeautifulSoup(page.read())
	p = re.compile( '(Live Scorecard | ESPN Cricinfo)')
	soup=p.sub( ' ', str(soup))
	soup = BeautifulSoup(soup)
	message=soup.find("title")
	message=message.string
	os.system('notify-send "Score" "'+message+'"')
	time.sleep(10)