from bs4 import *
import requests
import re

def main():


	e1 = input('Enter the artist :')
	e2 = input('Enter the song name :')
	artist=''        #final string artist
	song=''          #final string song
	for i in e1:
		if i==' ':
			artist=artist+'-'
		else: artist=artist+i
	for i in e2:
		if i==' ':
			song=song+'-'
		else: song=song+i
	#print(artist)
	#print(song)

	url = 'http://www.metrolyrics.com/'+song+'-lyrics-'+artist+'.html'
	#print(url)
	data = requests.get(url)
	soup = BeautifulSoup(data.text,'html.parser')
	#print(soup)
	data2 = soup.find_all('p',{'class':'verse'})
	#print(data2)
	data3=re.sub('<br/>','',str(data2))
	data4=re.sub('<p class="verse">','\n\n',str(data3))
	data5=re.sub('</p>',' ',str(data4))
	data6=re.sub('<br>','',str(data5))
	data7=re.sub('</br>','',str(data6))
	#print(data7)

	mainString=''  #using a new string to store data5 after removing '[' and ']' 
	for i in data7:
		if (i=='[' or i==']'):
			mainString=mainString+' '
		else: mainString=mainString+i

	print(mainString)

if __name__ == '__main__':main() 