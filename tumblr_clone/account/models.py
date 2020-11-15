from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    birth_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"@{self.username}"
