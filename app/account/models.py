from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_TYPES = (
        ('women', 'women'),
        ('men', 'men'),
    )

    email = models.EmailField('Email', unique=True, max_length=40)
    phone_number = models.CharField('Phone', max_length=12, blank=True, null=True)
    auth_code = models.CharField(max_length=6, blank=True)
    invite_code = models.CharField(max_length=6, blank=True)
    has_used_invite = models.BooleanField(default=False)
    name = models.CharField('Name', max_length=255, blank=True, default='')
    avatar = models.ImageField('Foto', upload_to='', blank=True, null=True)
    gender = models.CharField('Gender', choices=GENDER_TYPES, max_length=10, null=True, blank=True)
    is_active = models.BooleanField('Active', default=True)
    is_superuser = models.BooleanField('SuperUser', default=False)
    is_staff = models.BooleanField('Admin', default=False)
    date_joined = models.DateTimeField('Date Join', default=timezone.now)
    last_login = models.DateTimeField('Last Login', auto_now_add=True, blank=True, null=True)
    auth_code_created_at = models.DateTimeField('Date', auto_now_add=True, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('email',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
