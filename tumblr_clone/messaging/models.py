from django.db import models
from django.urls import reverse
from account.models import User
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-sent_on']
    def __str__(self):
        return str(self.sender) + ' > ' + str(self.receiver)+' '+str(self.pk)
    def get_absolute_url(self):
        return reverse("message:list")
