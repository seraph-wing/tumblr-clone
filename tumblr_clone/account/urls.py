
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.AccountIndex.as_view(),name='account_index'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
]
