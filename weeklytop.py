import requests
from bs4 import BeautifulSoup

url="http://www.saavn.com/s/featured/hindi/Weekly+Top+Songs" 
r=requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
link = soup.find_all("li",{"class":"song-wrap"})

for item in link :
	print item.find_all("div",{"class":"index"})[0].text +" -> "+item.find_all("span",{"class":"title"})[0].text
	print "Album -> "+item.find_all("a",{"class":"meta-album"})[0].text
	print "Artist -> "+item.find_all("a",{"class":"multi-meta"})[0v].text
	print "Year -> "+item.find_all("a",{"class":"meta-year"})[0].text
	print '\n \n'