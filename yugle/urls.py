from django.conf.urls import url, include
from . import views

app_name = 'yugle'

urlpatterns = [
    url(r'^home/$', views.HomePageView.as_view(), name='homePage'),
    url(r'^results/$', views.SearchResultsView.as_view(), name='searchResults'),
    ]
