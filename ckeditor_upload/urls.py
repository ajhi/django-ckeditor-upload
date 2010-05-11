from django.conf.urls.defaults import *
from views import upload, test

urlpatterns = patterns('',
    (r'^$', test),
    (r'^upload/$', upload),
)