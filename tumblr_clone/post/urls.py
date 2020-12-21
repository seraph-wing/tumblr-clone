from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'post'


urlpatterns = [
    path('create',views.CreatePost.as_view(),name='create'),
]
