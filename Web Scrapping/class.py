#Printing particular class(html) using web scrapping.


import requests
import bs4
import lxml

result = requests.get("https://en.wikipedia.org/wiki/Elon_Musk")
soup = bs4.BeautifulSoup(result.text,"lxml")

#Getting table of content class.
soup.select('.toctext')

#Printing table of content class.
for item in soup.select('.toctext'):
	print(item.text)

