from django.conf.urls.defaults import *

from codefish.views import home

urlpatterns = patterns('',
    url(r'^$', 'codefish.views.home', name='home'),
    url(r'^$', 'codefish.views.hello', name='hello')
)
