import os
import urllib
#import urllib2
#import time 
import requests

from bs4 import BeautifulSoup




def main(i,j):
	print(" The pics will be stored in CyanideNhappiness directory")
	
	os.mkdir('CyanideNhappiness')
	os.chdir('./CyanideNhappiness/')
		
	while (i <= 4409) :
		
			
		url = "http://explosm.net/comics/" + str(i)
		
		
		request  = requests.get(url)
		var = request.text
		soup = BeautifulSoup(var,"html.parser")
		
		final_url = "https://" + soup.find("img",{"id":"main-comic"})['src'].strip("//") 

		urllib.urlretrieve(final_url, "./" + str(j) +".png")
		j += 1
		i += 1

main(4400,1)

