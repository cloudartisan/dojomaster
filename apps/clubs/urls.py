"""
from django.conf.urls import include, url

import views

from organizations.backends import invitation_backend
from organizations.urls import urlpatterns

# Extends organizations.urls.urlpatterns
urlpatterns += [
    url(r'^invitations/', include(invitation_backend().get_urls())),
]
"""

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ListClubView.as_view(), name='clubs-list',),
    url(r'^(?P<club_pk>[\d]+)/$', views.DetailClubView.as_view(), name='clubs-detail',),
    url(r'^(?P<club_pk>[\d]+)/edit$', views.UpdateClubView.as_view(), name='clubs-update',),
    url(r'^add/$', views.CreateClubView.as_view(), name='clubs-create',),
    url(r'^(?P<club_pk>[\d]+)/delete$', views.DeleteClubView.as_view(), name='clubs-delete',),
]
