from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from django.contrib.auth.models import UserManager
from utils import UserTypeChoices

class AbstractUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('username'),
                                  max_length=150,
                                  help_text="should be alpha only with max length 50",
                                  null=True)

    email = models.EmailField(_('email address'), validators=[EmailValidator], unique=True)

    phone = models.CharField(max_length=20, blank=True, null=True)

    user_type = models.SmallIntegerField(choices=UserTypeChoices.choices, default=UserTypeChoices.CUSTOMER)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True
        db_table = 'users'

    def __str__(self) -> str:
        return self.email

class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'