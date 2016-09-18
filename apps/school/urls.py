from django.conf.urls import include, url

import views

from organizations.backends import invitation_backend
from organizations.urls import urlpatterns

urlpatterns += [
    url(r'^invitations/', include(invitation_backend().get_urls())),
]
