from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'registration_page.views.home', name='home'),
    url(r'^authors$', 'registration_page.views.authors', name='authors'),
    url(r'^thank-you$', 'registration_page.views.thank_you', name='thank_you'),
    url(r'^title-and-abstract$', 'registration_page.views.title_and_abstract', name='title_and_abstract'),
    url(r'^details$', 'registration_page.views.details', name='details'),
    url(r'^sources$', 'registration_page.views.sources', name='sources'),

    # url(r'^journal_page/', include('journal_page.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
