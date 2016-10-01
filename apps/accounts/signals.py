from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserAccount, UserAccountProfile


@receiver(post_save, dispatch_uid="create_profile", sender=UserAccount)
def create_profile(sender, **kwargs):
    """
    Receives the post_save signal from UserAccount. If a UserAccount has been
    created, create and save the UserAccountProfile linked to it.
    """
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserAccountProfile(user=user)
        user_profile.save()
