from django.shortcuts import render

from django.views import generic
from models import Keyword, SiteInfo

class HomePageView(generic.TemplateView):
    template_name = 'yugle/homepage.html'

class SearchResultsView(generic.ListView):
    template_name = 'yugle/resultspage.html'

