from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ListClassView.as_view(), name='classes-list',),
    url(r'^(?P<class_pk>[\d]+)/$', views.DetailClassView.as_view(), name='class-detail',),
    url(r'^(?P<class_pk>[\d]+)/edit$', views.UpdateClassView.as_view(), name='class-update',),
    url(r'^add/$', views.CreateClassView.as_view(), name='class-create',),
    url(r'^(?P<class_pk>[\d]+)/delete$', views.DeleteClassView.as_view(), name='class-delete',),
]
