from django.contrib import admin
from .models import Post, Note, Like, Reblog
# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Note)
admin.site.register(Reblog)
