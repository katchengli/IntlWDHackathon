from django.conf.urls import patterns, url
from management import views

urlpatterns = patterns('',
	url(r'^$', views.management, name='management'),
	# url(r'^new', views.new, name='new')
)