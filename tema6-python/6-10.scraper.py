# coding=utf-8

import requests
import bs4
# sudo pip install requests beautifulsoup4
# docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# obtenemos el html de la página
# requests http://www.python-requests.org/en/master/
response = requests.get('http://www.elpais.com/')


# pasamos el html a BeaytifulSoupt
soup = bs4.BeautifulSoup(response.text, "html5lib")


# buscamos los links e imprimimos su texo y url
links = soup.select('h2')

for link in links:
    print link.text, ' ', link.attrs.get('href')
