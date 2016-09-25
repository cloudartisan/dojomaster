"""
http://django-organizations.readthedocs.io/en/latest/usage.html

The OrganizationSignup view is used for allowing a user new to the site to
create an organization and account. This view relies on the registration
backend to create and verify a new user.
"""

from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from organizations.mixins import OrganizationMixin, AdminRequiredMixin
from organizations.views import (BaseOrganizationList, BaseOrganizationDetail,
                                 BaseOrganizationCreate, BaseOrganizationUpdate,
                                 BaseOrganizationDelete)

from models import Club


class ClubViewMixin(LoginRequiredMixin):
    model = Club


class ClubOwnerViewMixin(ClubViewMixin, OrganizationMixin):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.organization = self.get_organization()
        self.club = self.organization.provider
        if not self.organization.is_admin(request.user) and not \
                self.club.is_member(request.user):
            return HttpResponseForbidden(("Sorry, club owners only"))
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)


class ClubList(ClubViewMixin, BaseOrganizationList):
    pass


class ClubDetail(ClubViewMixin, BaseOrganizationDetail):
    pass


class ClubUpdate(ClubOwnerViewMixin, BaseOrganizationUpdate):
    pass


class ClubCreate(ClubViewMixin, BaseOrganizationCreate):
    pass


class ClubDelete(ClubOwnerViewMixin, BaseOrganizationDelete):
    pass
