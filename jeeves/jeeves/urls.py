import settings
from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Auto discover for the admin site
from django.contrib import admin
admin.autodiscover()

# Auto discover for dajaxice
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Redirect login attempts
    (r'^accounts/login', redirect_to, {'url': '/account/login'}),

    url(r'^$', 'core.views.index'),

    url(r'^account$', 'core.views.account_index'),
    url(r'^account/confirm/(?P<activation_key>[\w-]+)$', 'core.views.account_activate'),
    url(r'^account/edit$', 'core.views.account_edit'),
    url(r'^account/delete/(?P<account_id>[\w-]+)$', 'core.views.account_delete'),
    url(r'^account/login$', 'core.views.account_login'),
    url(r'^account/logout$', 'core.views.account_logout'),
    url(r'^account/lost_password$', 'core.views.account_lost_password'),
    url(r'^account/register$', 'core.views.account_register'),
    url(r'^account/register/complete$', 'core.views.account_register_complete'),

    url(r'^cloud$', 'cloud.views.list'),
    url(r'^cloud/add$', 'cloud.views.add'),
    url(r'^cloud/(?P<uuid>[\w-]+)$', 'cloud.views.index'),
    url(r'^cloud/(?P<uuid>[\w-]+)/edit$', 'cloud.views.edit'),
    url(r'^cloud/(?P<uuid>[\w-]+)/security_group$', 'cloud.views.security_group_list'),
    url(r'^cloud/(?P<uuid>[\w-]+)/security_group/add$', 'cloud.views.security_group_add'),

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Dajax ice URLs
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)
