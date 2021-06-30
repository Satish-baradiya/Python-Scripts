#This would work only if the thumbnail image is present in .thumbimage class.

import requests
import bs4
import lxml

result = requests.get("https://en.wikipedia.org/wiki/Elon_Musk")
soup = bs4.BeautifulSoup(result.text,"lxml")
image = soup.select('.thumbimage')[0]

print(image['src'])