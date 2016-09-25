from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.ListGradingView.as_view(), name='gradings-list',),
    url(r'^(?P<grading_pk>[\d]+)/$', views.DetailGradingView.as_view(), name='grading-detail',),
    url(r'^(?P<grading_pk>[\d]+)/edit$', views.UpdateGradingView.as_view(), name='grading-update',),
    url(r'^add/$', views.CreateGradingView.as_view(), name='grading-create',),
    url(r'^(?P<grading_pk>[\d]+)/delete$', views.DeleteGradingView.as_view(), name='grading-delete',),
]
