from django.db import models
from django.urls import reverse
from account.models import User
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    POST_CHOICES = [
    ('TXT','Text'),
    ('Q','Quote'),
    ('IMG','Image'),
    ('VID','Video'),
    ('GIF','GIF'),
    ('AUD','Audio'),
    ]
    post_type = models.CharField( max_length=3,choices=POST_CHOICES,default='TXT')
    title = models.CharField(max_length=128,blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='post/images/',blank=True,null=True)
    video = models.FileField(upload_to='post/videos/',blank=True,null=True)
    gif = models.FileField(upload_to='post/gifs/',blank=True,null=True)
    audio = models.FileField(upload_to='post/audio/',blank=True,null=True)
    op = models.ForeignKey(User,on_delete=models.CASCADE)
    is_reblogged = models.BooleanField(default=False,blank=True)
    tags = TaggableManager()#to manage tagging
    notes = models.ForeignKey('Note', on_delete=models.CASCADE)

class Note(models.Model):
    pass
