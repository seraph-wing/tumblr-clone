from django.db import models
from django.urls import reverse
from account.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    POST_TYPE_CHOICES = [
    ('TXT','Text'),
    ('Q','Quote'),
    ('IMG','Image'),
    ('VID','Video'),
    ('GIF','GIF'),
    ('AUD','Audio'),
    ]
    POST_WHEN_CHOICES = [
        ('NOW','Post Now'),
        ('QU','Add to queue'),
        ('DR','Add to draft'),
        ('PR','Post privately'),
        ('SC','Schedule'),
    ]
    post_type = models.CharField( max_length=3,choices=POST_TYPE_CHOICES,default='TXT')
    title = models.CharField(max_length=128,default=' ')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='post/images/',blank=True,null=True)
    video = models.FileField(upload_to='post/videos/',blank=True,null=True)
    gif = models.FileField(upload_to='post/gifs/',blank=True,null=True)
    audio = models.FileField(upload_to='post/audio/',blank=True,null=True)
    op = models.ForeignKey(User,on_delete=models.CASCADE)
    is_reblogged = models.BooleanField(default=False,blank=True)
    tags = TaggableManager(blank=True)#to manage tagging
    posted_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    source = models.URLField(blank=True)
    quote_text = models.TextField(blank=True)
    post_when = models.CharField(max_length=3,choices=POST_WHEN_CHOICES,default='NOW')
    scheduled_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post:detail",kwargs={"username":self.op.username,"pk":self.pk})

#defining the relations
class Note(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.TextField()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = [['post','user']]#so that a user cannot like a post more than once
        ordering = ['-liked_on']#ordering on liked on so it is returned in descending order


class Reblog(models.Model):
    reblogger = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reblogger')
    parent_post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='parent_post')
    reblogged_content = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='reblogged_content')
    def __str__(self):
        return 'reblog | '+str(self.id)
