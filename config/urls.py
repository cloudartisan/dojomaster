from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from apps.base.views import NameChange

handler500 = 'utils.views.server_error'

urlpatterns = []

# Debug/Development URLs
if settings.DEBUG is True:
    urlpatterns += [
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    ]

# Includes
urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
]

# Project URLs
urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/name/$', NameChange.as_view(), name='account_change_name'),
]

# Application URLs
urlpatterns += [
    url(r'^dashboard/', include('apps.dashboard.urls')),
    url(r'^clubs/', include('apps.clubs.urls')),
    url(r'^schools/', include('apps.schools.urls')),
    url(r'^classes/', include('apps.classes.urls')),
    url(r'^students/', include('apps.students.urls')),
    url(r'^attendance/', include('apps.attendance.urls')),
    url(r'^gradings/', include('apps.gradings.urls')),
]
