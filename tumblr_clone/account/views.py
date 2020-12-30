from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,TemplateView,UpdateView
from django.views.generic.detail import DetailView
from . import forms
from django.urls import reverse_lazy,reverse
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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
    def get_success_url(self,*args,**kwargs):

        return reverse_lazy('account:account_index',kwargs={'slug':self.request.user.slug})

def follow(request,pk):
    user_to_be_followed = get_object_or_404(User,id=request.POST.get('user_id_follow'))
    user_to_be_followed.followers.add(request.user)
    return HttpResponseRedirect(reverse('account:account_index',args=[user_to_be_followed.slug]))

def unfollow(request,pk):
    user_to_be_unfollowed = get_object_or_404(User,id=request.POST.get('user_id_unfollow'))
    user_to_be_unfollowed.followers.remove(request.user)
    return HttpResponseRedirect(reverse('account:account_index',args=[user_to_be_unfollowed.slug]))
