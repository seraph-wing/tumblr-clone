from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
# Create your views here.

class AccountIndex(TemplateView):
    template_name = 'account/account_index.html'
