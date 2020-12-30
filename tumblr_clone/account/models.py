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
    followers = models.ManyToManyField("User",blank=True,symmetrical=False,related_name='is_followed_by')

    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('account:account_index', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        self.slug = slugify(self.username)
        return super().save(*args,**kwargs)

#adding oneself as one's own follower:
from django.db.models.signals import post_save
def add_default_follower(sender, instance, **kwargs):
   instance.followers.add(instance)
post_save.connect(add_default_follower, sender=User)
