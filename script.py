import os
try:
	import urllib,urlparse,requests,multiprocessing
	from bs4 import BeautifulSoup
except ImportError:
	raise ImportError("Module not installed")



def download_comic():
	print(" The pics will be stored in CyanideNhappiness directory  \n")
	
	os.mkdir('CyanideNhappiness')
	os.chdir('./CyanideNhappiness/')
	i = 15
	while (str(i) != 'latest') :
		
			
		url = "http://explosm.net/comics/" + str(i)
		
		var = requests.get(url).text
		
		soup = BeautifulSoup(var,"html.parser")
		
		try:
			final_url = "https://" + soup.find("img",{"id":"main-comic"})['src'].strip("//") 
			u = urlparse.urlparse(final_url).path.split('/')[-1]
			urllib.urlretrieve(final_url, u)
		
		except TypeError as e:
			print "Comic not found"
			
		i += 1



if __name__ == "__main__":
	
	download_comic()


#Todo: check if 'latest' referrer header is specified in BeautifulSoup object.