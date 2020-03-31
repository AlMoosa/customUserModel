from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    phone_number = PhoneNumberField(max_length=16,
                                     help_text='Введите ваш номер', unique=True)
    location = models.CharField(max_length=30,
                                help_text='Ваше местоположение')
    date_joined = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user.username
