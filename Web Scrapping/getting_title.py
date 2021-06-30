#Getting title of wikipedia article using web scrapping.


import requests
import bs4
import lxml
result = requests.get("https://en.wikipedia.org/wiki/Elon_Musk")
result
soup = bs4.BeautifulSoup(result.text,"lxml")
soup.select('title')[0].getText()
