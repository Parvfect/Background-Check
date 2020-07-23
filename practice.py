import bs4 as bs
import urllib.request
import sys

doc = 'ok bois'
wikipedia = "https://en.wikipedia.org/wiki/"

def check(url, term):
    return url.startswith(term)

def wiki(url):
    doc = ''
    sentence = ''
    check(url, wikipedia)
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    for paragraph in soup.find_all('p'):
        doc += str(paragraph.text)
    doc = doc.split()
    for i in doc:
        sentence += i+" "
        if i.endswith('.'):
            print(sentence)
            print("\n\n")

        


wiki("https://en.wikipedia.org/wiki/George_Washington")