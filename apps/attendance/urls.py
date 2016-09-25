from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ListAttendanceView.as_view(), name='attendance-list',),
    url(r'^(?P<attendance_pk>[\d]+)/$', views.DetailAttendanceView.as_view(), name='attendance-detail',),
    url(r'^(?P<attendance_pk>[\d]+)/edit$', views.UpdateAttendanceView.as_view(), name='attendance-update',),
    url(r'^add/$', views.CreateAttendanceView.as_view(), name='attendance-create',),
    url(r'^(?P<attendance_pk>[\d]+)/delete$', views.DeleteAttendanceView.as_view(), name='attendance-delete',),
]
