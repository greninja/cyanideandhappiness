try:
	import os
	import urllib
	import urlparse
	import requests
	import argparse
	from multiprocessing import Pool
	from bs4 import BeautifulSoup

except ImportError:
	raise ImportError("Module not installed")


def changeDiretory():


	print(" The pictures will be stored in CyanideNhappiness directory  \n")
	
	if not os.path.exists('CyanideNhappiness'):
		os.makedirs('CyanideNhappiness')

	os.chdir('CyanideNhappiness')

	return


def download_comic(starting_index):
	
	
	# Actual index where the downloading of comics begin
	index = starting_index
	
	while True :
		
			
		url = "http://explosm.net/comics/" + str(index)
		htmlstring = requests.get(url).text
		
		# Making a Beautiful Soup object to parse the html file
		soup = BeautifulSoup(htmlstring,"html.parser")
		
		try:
			final_url = "https://" + soup.find("img",{"id":"main-comic"})['src'].strip("//") 
			parsed_url = urlparse.urlparse(final_url).path.split('/')[-1]
			urllib.urlretrieve(final_url, parsed_url)
		
			if soup.find("a",{"title":"Latest comic"})['class'][0] == 'disabled':
				break
		
		except TypeError:
			pass

		index += 1

	print "Finished Downloading!"


if __name__ == "__main__":
	
	changeDiretory()
	
	parser = argparse.ArgumentParser("Parse an integer for starting index")
	parser.add_argument('startindex',action='store',default = '15',type=int,
   		                  help = 'An index of where the user wants the download to start from')

	args = parser.parse_args()

	download_comic(args.startindex)