from django.db import models
from .ModelHandlers.google_search_scraper import *
from .ModelHandlers.news_article_scraper import *

# Create your models here.

class ModelController:
    def __init__(self):
        self.news_search_strings = ['christchruch cbd developments'];
        self.new_article_urls = []
        self.google_search_scraper = GoogleSearchScraper()
        self.article_scraper = ArticleScraper()

    def get_news_article_urls(self):
        self.new_article_urls.append(self.google_search_scraper.get_news_article_urls(self.news_search_strings))
    
    def get_news_article_content(self, url):
        article_string = self.article_scraper.get_article_content(url)
        return article_string
