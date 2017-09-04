import bs4
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


url_1 = "https://www.stuff.co.nz/the-press/news/95661149/the-future-isnt-going-anywhere-so-why-did-christchurch-rebuild-the-city-of-yesterday"
url_2 = "https://www.stuff.co.nz/the-press/news/96103281/work-starts-on-40-million-new-sudima-hotel"

current_page = urlopen(url_2)
page_html = current_page.read()
current_page.close()

page_soup = BeautifulSoup(page_html, "html.parser")

article = page_soup.find("article")
article.div.clear()
article.div.clear()
content = page_soup.find_all("p")


text = re.split("- Stuff", str(content))

