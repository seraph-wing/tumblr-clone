from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'message'

urlpatterns = [
    path('conversations/', views.Converstaions.as_view(),name='conversations'),
    path('messages/<int:pk>',views.AllMessagesByUser.as_view(),name='user_list'),
]
