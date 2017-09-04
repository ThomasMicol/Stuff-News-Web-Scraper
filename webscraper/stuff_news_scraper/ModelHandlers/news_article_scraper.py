import bs4
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


class ArticleScraper:

    def get_article_content(self, url):
        opened_page = urlopen(url)
        page_html = opened_page.read()
        opened_page.close();
        soup = BeautifulSoup(page_html, "html.parser")
        article = soup.find("article")
        article.div.clear()
        article.div.clear()
        content = soup.find_all("p")
        return str(re.split("- Stuff", str(content)))