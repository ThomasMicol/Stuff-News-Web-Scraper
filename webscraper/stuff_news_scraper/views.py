from django.shortcuts import render
from django.http import HttpResponse
from .models import *



def get_dashboard(request):
    myModel = ModelController()
    string = "<h1>This is the Dashboard</h1> "
    string += myModel.get_news_article_content("https://www.stuff.co.nz/the-press/news/96103281/work-starts-on-40-million-new-sudima-hotel")
    return HttpResponse(string)
# Create your views here.
