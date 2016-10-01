from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from allauth.account.models import EmailAddress
from phonenumber_field.modelfields import PhoneNumberField


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('E-mail Address'),
        max_length=255,
        unique=True,
        blank=False,
        help_text=_('Required. 255 characters or fewer.'),
        error_messages={
            'unique': _("A user with that e-mail address already exists."),
        },
    )
    is_staff = models.BooleanField(
        verbose_name=_('Staff Status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date Joined'),
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        verbose_name=_('Date Updated'),
        auto_now=True,
    )

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        # __unicode__ on Python 2
        return self.email


@python_2_unicode_compatible
class UserAccountProfile(models.Model):
    user = models.OneToOneField(UserAccount, related_name='profile')
    picture = models.ImageField(
        verbose_name=_('Profile Picture'),
        upload_to='profile_images',
        blank=True
    )
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        # __unicode__ on Python 2
        return "{} profile".format(self.user.email)

    class Meta:
        db_table = 'accounts_useraccount_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False


UserAccount.profile = property(lambda u: UserAccountProfile.objects.get_or_create(user=u)[0])
