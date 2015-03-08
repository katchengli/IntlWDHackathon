from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns('',
	url(r'^$', views.products, name='products'),
)