from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ListSchoolView.as_view(), name='schools-list',),
    url(r'^(?P<school_pk>[\d]+)/$', views.DetailSchoolView.as_view(), name='schools-detail',),
    url(r'^(?P<school_pk>[\d]+)/edit$', views.UpdateSchoolView.as_view(), name='schools-update',),
    url(r'^add/$', views.CreateSchoolView.as_view(), name='schools-create',),
    url(r'^(?P<school_pk>[\d]+)/delete$', views.DeleteSchoolView.as_view(), name='schools-delete',),
]
