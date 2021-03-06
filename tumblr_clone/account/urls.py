from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'


urlpatterns = [
    path('<slug:slug>',views.AccountIndex.as_view(),name='account_index'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('edit/<slug:slug>', views.UpdateUserView.as_view(),name='edit'),
    path('follow/<int:pk>',views.follow,name='follow'),
    path('unfollow/<int:pk>',views.unfollow,name='unfollow'),
    path('likes/<slug:slug>',views.LikeView.as_view(),name='likes'),
]
