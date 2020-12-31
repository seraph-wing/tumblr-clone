from django.contrib import admin
from .models import Post, Note, Like, Reblog

# Register your models here.
#INLINE CLASSES FOR ACTIONS
class LikeInline(admin.TabularInline):
    model = Like
    extra = 1
class NoteInline(admin.TabularInline):
    model = Note
    extra = 1
class ReblogInline(admin.TabularInline):
    model = Reblog
    fk_name='parent_post'
    extra = 1
#ADMIN CLASS FOR DISPLAYING THE ACTIONS FIELDS
class PostAdmin(admin.ModelAdmin):
    inlines = (LikeInline,NoteInline,ReblogInline)

admin.site.register(Post,PostAdmin)
admin.site.register(Like)
admin.site.register(Note)
admin.site.register(Reblog)
