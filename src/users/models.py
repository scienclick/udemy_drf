from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.BigIntegerField(verbose_name="Contact Phone", blank=True, null=True,default=0)
