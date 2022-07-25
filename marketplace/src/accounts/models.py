from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, password, **extra_fields):
        if not email:
            raise ValueError(_('User must have a email address'))
        if not user_name:
            raise ValueError(_('User must have a user name'))

        email = self.normalize_email(email)
        slug = slugify(user_name)
        user = self.model(email=email, user_name=user_name, slug=slug, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(email, user_name, password, **extra_fields)

"""
CustomUser
- email (email)
- user_name (char)
- first_name (char)
- last_name (char)
- Slug (slug)
- is_active (boolean)
- is_staff (boolean)
- is_superuser (boolean)
"""
class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.CharField(max_length=200, unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    objects = CustomUserManager()

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def __str__(self):
        return self.user_name
