from django.conf.urls import patterns, url

from materials import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# url(r'^new', views.new, name='new')
