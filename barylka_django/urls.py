from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.base import RedirectView
from django.conf import settings
urlpatterns = patterns('',

     url(r'^$', 'barylka_django.web.views.index', name='index'),
     url(r'^edycja/'+ str(settings.CURRENT_BARYLKA_EDITION) + r'/$', RedirectView.as_view(url='/', permanent=False)),
     url(r'^edycja/(\d)/$', 'barylka_django.web.views.index', name='index'),

     url(r'^ranking/$', 'barylka_django.web.views.rank', name='rank'),
     url(r'^ranking/'+ str(settings.CURRENT_BARYLKA_EDITION) + r'/$', RedirectView.as_view(url='/ranking/', permanent=False)),
     url(r'^ranking/(\d)/$', 'barylka_django.web.views.rank', name='rank'),

     url(r'^ludzie/([\w-]*)/$', 'barylka_django.web.views.user', name='user'),
     url(r'^crawl$', 'barylka_django.crawler.micro_crawler.crawl', name='crawl'),

     url(r'^regulamin/', 'barylka_django.web.views.tos', name='tos'),

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
