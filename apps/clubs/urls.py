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
    url(r'^$', views.ClubList.as_view(), name='clubs-list',),
    url(r'^(?P<club_pk>[\d]+)/$', views.ClubDetail.as_view(), name='club-detail',),
    url(r'^(?P<club_pk>[\d]+)/edit$', views.ClubUpdate.as_view(), name='club-update',),
    url(r'^add/$', views.ClubCreate.as_view(), name='club-create',),
    url(r'^(?P<club_pk>[\d]+)/delete$', views.ClubDelete.as_view(), name='club-delete',),
]
