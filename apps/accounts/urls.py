from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import UserProfileChange


urlpatterns = [
    url(r'^profile/$', login_required(UserProfileChange.as_view()), name='user_profile_change'),
]
