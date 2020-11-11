from django.db import models
from django.contrib import auth
from django.utils import timezone
# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    profile_picture = models.ImageField(upload_to="profiel_pictures",blank =True, null= True, verbose_name='image1')
    def __str__(self):
        return "@{}".format(self.username)
