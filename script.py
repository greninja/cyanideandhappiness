import os
try:
	import urllib,urlparse,requests,multiprocessing
	from bs4 import BeautifulSoup
except ImportError:
	raise ImportError("Module not installed")



def download_comic():
	
	print(" The pictures will be stored in CyanideNhappiness directory  \n")
	
	os.mkdir('CyanideNhappiness')
	os.chdir('./CyanideNhappiness/')
	
	# Actual index where the comics begin
	i = 15
	
	while True :
		
			
		url = "http://explosm.net/comics/" + str(i)
		var = requests.get(url).text
		
		# Making a Beautiful Soup object to parse the html file
		soup = BeautifulSoup(var,"html.parser")
		
		try:
			final_url = "https://" + soup.find("img",{"id":"main-comic"})['src'].strip("//") 
			parsed_url = urlparse.urlparse(final_url).path.split('/')[-1]
			urllib.urlretrieve(final_url, parsed_url)
		
		except TypeError:
			pass

			
		if soup.find("a",{"title":"Latest comic"})['class'][0] == 'disabled':
			break

		i += 1

	print "Finished Downloading!"

if __name__ == "__main__":
	
	download_comic()




