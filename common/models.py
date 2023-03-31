from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=False)
    nickname = models.CharField(max_length=50, unique=True, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11, unique=True, blank=False)
    first_name = None
    last_name = None