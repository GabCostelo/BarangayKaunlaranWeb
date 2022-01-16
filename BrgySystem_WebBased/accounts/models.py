from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_BrgyStaff = models.BooleanField(default=False)
    is_Constituent = models.BooleanField(default=False)

class BrgyStaff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Constituent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
