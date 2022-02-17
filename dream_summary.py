# I have a dream - Web Scrape and Summary
from collections import Counter
import re, requests, bs4, nltk
from nltk.corpus import stopwords

def main():
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elems = [element.text for element in soup.find_all('p')]

    speech = ''.join(p_elems)

    
