from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

class UserManger(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set.")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, password=None, **extra_feilds):
        extra_feilds.setdefault('is_staff', False)
        extra_feilds.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_feilds)

    def create_superuser(self, email, password, **extra_feilds):
        extra_feilds.setdefault('is_staff', True)
        extra_feilds.setdefault('is_superuser', True)

        if extra_feilds.get('is_superuser') is True:
            get_user_model().objects.filter(is_superuser=True).update(
            first_name="Velder", last_name="Mont"
        )

        if extra_feilds.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_feilds.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_feilds)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManger()

