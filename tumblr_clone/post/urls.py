from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'post'


urlpatterns = [
    path('create',views.CreatePost.as_view(),name='create'),
    path('view/<username>/<int:pk>',views.PostDetail.as_view(),name='detail'),
    path('dashboard',views.Dashboard.as_view(),name='dashboard'),
]
