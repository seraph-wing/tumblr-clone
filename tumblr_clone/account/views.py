from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView
from django.views.generic.detail import DetailView
from . import forms
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AccountIndex(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'account/account_index.html'

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    exclude = ('followers',)
    template_name = 'account/signup.html'

class LoginView(TemplateView):
    template_name = 'account/login.html'

class UpdateUserView(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['description', 'profile_picture']
    template_name = 'account/edit_user.html'
    slug_field = 'slug'
    #success_url = reverse_lazy('account:account_index',kwargs={'slug':model.slug})
    def get_success_url(self,*args,**kwargs):

        return reverse_lazy('account:account_index',kwargs={'slug':self.request.user.slug})
