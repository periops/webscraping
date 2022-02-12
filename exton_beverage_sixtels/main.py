from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://extonbeverage.com/shop-products/category/2144-p1-6-keg.html').text
soup = BeautifulSoup(html_text, 'lxml')
kegs = soup.find_all('div', class_ = 'hkc-md-4')

for keg in kegs:
    beer_name = keg.find('span', class_ = 'hikashop_product_name').text.lstrip().replace(' 1/6 keg', '')
    keg_price = keg.find('span', class_ = 'hikashop_product_price').text

#need to figure out how to do a google search for the beer name and then scrape the abv and the rating from beeradvocate.com

    print(f'''
    Beer: {beer_name}
    Keg Price: {keg_price}
    ''')