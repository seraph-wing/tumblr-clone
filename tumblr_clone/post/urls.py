from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'post'


urlpatterns = [
    path('create',views.CreatePost.as_view(),name='create'),
    path('view/<username>/<int:pk>',views.PostDetail.as_view(),name='detail'),
    path('dashboard',views.Dashboard.as_view(),name='dashboard'),
    path('delete/<int:pk>',views.PostDelete.as_view(),name='delete'),
    path('edit/<int:pk>',views.EditPost.as_view(),name='edit'),
    path('view/<username>',views.UserPosts.as_view(),name='user_posts'),
    path('like/<int:pk>',views.like,name='like'),
    path('unlike/<int:pk>',views.unlike,name='unlike'),
    path('reblog/<int:pk>',views.ReblogPost.as_view(),name='reblog'),
    path('add_note/<int:pk>',views.AddNote.as_view(),name='add_note'),
    path('note_list/<int:pk>',views.NotesList.as_view(),name='note_list'),
]
