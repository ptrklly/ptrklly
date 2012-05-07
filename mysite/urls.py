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
    (r'^safespace', 'polls.views.safespace'),
    (r'^login', 'polls.views.login'),
    (r'^contact', 'polls.views.contact'),
    (r'^thanks', 'polls.views.thanks'),
    (r'^register', 'polls.views.register'),
    (r'^jack', 'polls.views.create_search_profile'),



)