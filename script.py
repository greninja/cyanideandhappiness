import os
import urllib
import urlparse
import requests

from bs4 import BeautifulSoup




def main(i,j):
	print(" The pics will be stored in CyanideNhappiness directory")
	
	os.mkdir('CyanideNhappiness')
	os.chdir('./CyanideNhappiness/')
		
	while (i <= 4409) :
		
			
		url = "http://explosm.net/comics/" + str(i)
		
		
		
		var = requests.get(url).text
		soup = BeautifulSoup(var,"html.parser")
		
		final_url = "https://" + soup.find("img",{"id":"main-comic"})['src'].strip("//") 
		u = urlparse.urlparse(final_url).path.split('/')[-1]
		urllib.urlretrieve(final_url, u)
		j += 1
		i += 1

main(4400,1)

