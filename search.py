import bs4 as bs
import urllib.request   
from googlesearch import search
import sys

query = "Saurav Sabu"
urls = []
for j in search(query, tld = 'co.in', num = 10, start = 0, stop = None, pause = 2.0):
    urls.append(j)

    for i in urls:
        try:
            source = urllib.request.urlopen(i).read()
            soup = bs.BeautifulSoup(source, "lxml")
            for url in soup.find_all('a'):
                print(url.get('href'))
        except:
            e = sys.exc_info()[0]
            print("Exception occured", e)



