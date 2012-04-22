from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),

    (r'^$', 'polls.views.home'),
    (r'^base/', 'polls.views.base'),
    (r'^cv', 'polls.views.cv'),

)