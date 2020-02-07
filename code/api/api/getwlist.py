import re
import requests
from brow.interface.simple import SimpleFirefoxBrowser as SimpleBrowser
from bs4 import BeautifulSoup
from pprint import pprint

def get_wishlist(wishlist_id):
    divider = '<body '
    l = []
    with SimpleBrowser.session() as b:
        loc = 'https://www.amazon.com/hz/wishlist/ls/%s' % wishlist_id
        b.load(loc)
        s = str(b.soup)
        s = divider + s.split(divider)[-1]
        s = BeautifulSoup(s, "html.parser")
        divs = s.findAll("div", {"id": re.compile('^itemImage_')})
        for div in divs:
            img = div.find("img")['src']
            span = div.find('a')['title']
            link = 'https://www.amazon.com/' + div.find('a')['href'].lstrip('/')
            l.append({'img': img, 'name': span, 'url': link})
        # print(divs)
    return l

if __name__ == '__main__':
    get_wishlist('2ZHXUYP0TYC5E')
