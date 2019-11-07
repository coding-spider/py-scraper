import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
response = http.request('GET', 'https://github.com/')

html = BeautifulSoup(response.data)

print(html)
