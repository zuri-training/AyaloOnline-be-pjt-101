import requests

from bs4 import BeautifulSoup

URL="https://www.bigrentz.com/blog/construction-equipment-names"

r=requests.get(URL)

soup=BeautifulSoup(r.text, 'html5lib')



with open ('construction.html','w') as htmlfile:
	htmlfile.write(soup.prettify())