from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth import get_user_model

User = get_user_model()
class Ban(models.Model):
    licenseID = models.ForeignKey(User, related_name="licenseIDUser", on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.licenseID)

from django.contrib.auth.models import User
# Create your models here.
class User(User, PermissionsMixin):
    def __str__(self):
        return "{}".format(self.username)


