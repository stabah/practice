from django.conf.urls import patterns, include, url
from django.contrib import admin

from control_panel import settings
from control_panel.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'library.views.index'),
    url(r'^library/$', 'library.views.index'),
    url(r'^library/books/$', 'library.views.index'),
    url(r'^library/books/(\d+)/$', 'library.views.bookCard'),
    url(r'^library/authors/$', 'library.views.authors'),
    url(r'^library/authors/(\d+)/$', 'library.views.authorsCard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, }),
)
