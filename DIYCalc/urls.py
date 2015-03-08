from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DIYCalc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^materials/', include('materials.urls')),
    url(r'^management/', include('management.urls')),
    url(r'^home/', include('home.urls')),
<<<<<<< HEAD
    
=======
    url(r'^products/', include('products.urls')),
>>>>>>> origin/master
)
