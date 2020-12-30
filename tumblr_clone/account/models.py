from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class User(AbstractUser):
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    birth_date = models.DateField(null=True,blank=True)
    slug = models.SlugField(null=False,default='slugs')
    followers = models.ManyToManyField("User",blank=True,null=True,symmetrical=False,related_name='following')

    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('account:account_index', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args,**kwargs)
