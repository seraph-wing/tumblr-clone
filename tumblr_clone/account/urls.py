
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.AccountIndex.as_view(),name='account_index'),
]
