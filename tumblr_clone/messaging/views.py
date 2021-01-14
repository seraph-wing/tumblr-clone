from django.db.models import Q

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,TemplateView,UpdateView,ListView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Message
from account.models import User

class AllMessagesByUser(CreateView,LoginRequiredMixin):
    model = Message
    template_name = 'messaging/allmessages.html'
    fields = ['message']
    success_url = reverse_lazy('message:conversations')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user1 = self.request.user
        user2 = User.objects.get(pk=self.kwargs['pk'])
        context['user_messages'] = Message.objects.all().filter((Q(sender__exact=user1) & Q(receiver__exact=user2)) | (Q(sender__exact=user2) & Q(receiver__exact=user1)))
        return context
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user#adding the op as the one creating the post
        self.object.receiver = User.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)


class Converstaions(ListView):
    model = Message
    template_name = 'messaging/conversations.html'
    context_object_name = 'users'
    paginate_by = 40

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        users_interacted_with = set()
        all_messages = Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))
        for message in all_messages:
            if(message.sender==self.request.user):
                users_interacted_with.add(message.receiver)
            else:
                users_interacted_with.add(message.sender)
        context['interacted_users'] = users_interacted_with
        return context
