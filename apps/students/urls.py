from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ListStudentView.as_view(), name='students-list',),
    url(r'^(?P<student_pk>[\d]+)/$', views.DetailStudentView.as_view(), name='students-detail',),
    url(r'^(?P<student_pk>[\d]+)/edit$', views.UpdateStudentView.as_view(), name='students-update',),
    url(r'^add/$', views.CreateStudentView.as_view(), name='students-create',),
    url(r'^(?P<student_pk>[\d]+)/delete$', views.DeleteStudentView.as_view(), name='students-delete',),
]
