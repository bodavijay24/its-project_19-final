from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pie', views.pie, name='pie'),
	url(r'^house', views.house, name='house'),
	url(r'^get_details', views.get_details, name='get_details'),
	url(r'^medi', views.medi, name='medi'),
	url(r'^hh', views.hh, name='hh'),
	url(r'^well', views.well, name='well'),
	url(r'^farm', views.farm, name='farm'),
	url(r'^deal', views.deal, name='deal'),
	
	
]
