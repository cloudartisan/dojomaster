from django.conf.urls import url

from .views import UserProfileChange


urlpatterns = [
    url(r'^profile/$', UserProfileChange.as_view(), name='user_profile_change'),
]
