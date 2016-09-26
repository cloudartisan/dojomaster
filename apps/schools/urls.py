from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.SchoolList.as_view(), name='schools-list',),
    url(r'^(?P<school_pk>[\d]+)/$', views.SchoolDetail.as_view(), name='schools-detail',),
    url(r'^(?P<school_pk>[\d]+)/edit$', views.SchoolUpdate.as_view(), name='schools-update',),
    url(r'^add/$', views.SchoolCreate.as_view(), name='schools-create',),
    url(r'^(?P<school_pk>[\d]+)/delete$', views.SchoolDelete.as_view(), name='schools-delete',),
]
