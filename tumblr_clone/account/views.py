from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from . import forms

# Create your views here.
class HomeView(TemplateView):
    template_name = 'account/home.html'

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy("login")
    template_name = 'account/signup.html'
