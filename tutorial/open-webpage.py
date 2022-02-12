# open-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://extonbeverage.com/shop-products/category/2144-p1-6-keg.html'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

print(webContent[0:300])