import bs4 as bs
import urllib.request
from googlesearch import search
import sys

wikipedia = "https://en.wikipedia.org/wiki/"


def check(url, term):
    """Checks if the url is the specific site"""
    return url.startswith(term)

def searching(query, term):
    """Searches google to find the site that is needed"""
    item = query
    flag = False
    url = ""
    for j in search(query = item, tld = 'co.in', num = 10, start = 0, stop = None, pause = 2.0):   
        if check(j,term):
            flag = True
            url = j
            break
    control(url)    

def control(url):
    """Calls on the specific function for the site url to extract information"""
    wiki(url)

def wiki(url):
    """Extracts information from wikipedia"""
    doc, sentence = '',''
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    for paragraph in soup.find_all('p'):
        doc += str(paragraph.text)
    f = open(f"{search_query}.txt","w")
    f.write(doc)
    f.close()



search_query = input("Enter the term that is to be searched")
searching(search_query, "https://en.wikipedia.org/wiki/")