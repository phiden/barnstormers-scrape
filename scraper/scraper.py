import json
import requests
import re
from bs4 import BeautifulSoup

class Scraper(object):
    def __init__(self):
        self.url = "https://barnstormers.com/Piper,%20PA-28+Warrior%20Classifieds.htm"
    def scrape_site(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.content, 'html.parser')

        def has_ID(tag):
            return tag.has_attr('id')

        def isRed(color):
            return tag.has_attr('color')
            #return color and not re.compile("Green").search(color)

        if html:
            div = html.find_all(has_ID)
            data = []
            for item in div:
                text = item.find('b')
                url = item.find('a')
                #status = div.find(color="Red")
                #print status
                #print "\n"
                ad = item.find('p')
                location = item.find(string=re.compile("located"))
                data.append({
                    #'div' : str(item),
                    'title' : str(text),
                    'url' : str(url),
                    #'status' : str(status),
                    'ad' : str(ad),
                    'location' : location
                })
            return json.dumps(data, indent=2)

scraper = Scraper()
file = open("data.json", "w")
file.write(scraper.scrape_site())
file.close()
print(scraper.scrape_site())
