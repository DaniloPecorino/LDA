from requests import get
import re
from bs4 import BeautifulSoup

#   Scraper texts from http://www.gutenberg.org/browse/languages/it:
#   1.  scrape link from each element of the list
#   2.  open each link and download the txt file

url = 'http://www.gutenberg.org/browse/languages/it'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r"/ebooks/\d")
links = html_soup.find_all("a", href=pattern)

ebooks_links = []
for link in links:
    ebooks_links.append(link['href'])

utf8_pattern = re.compile(r".txt")
txt_links = []
counter = 1
for ebook in ebooks_links:
    print('{} out of {}'.format(counter, ebooks_links.__len__()))

    url = 'http://www.gutenberg.org'+ebook
    try:
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        txt_links.append('http:'+html_soup.find_all("a", href=utf8_pattern)[0]['href'])
    except:
        print('Not found')
        continue
    finally:
        counter = counter + 1



counter = 1
texts = []
for txt_link in txt_links:
    print('{} out of {}'.format(counter, ebooks_links.__len__()))
    try:
        texts.append(get(txt_link).text.replace("\n", "").replace("\r"," ")+"\n")
    except:
        continue
    finally:
        counter = counter + 1


with open('IT_text.txt', 'w') as f:
    for item in texts:
        f.write("%s\n" % item)
