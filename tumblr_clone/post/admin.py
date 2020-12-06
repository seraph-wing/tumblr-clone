from django.contrib import admin
from .models import Post, Notes, Likes, Reblogs
# Register your models here.
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Notes)
admin.site.register(Reblogs)
