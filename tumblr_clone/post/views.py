from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView,ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from endless_pagination.views import AjaxListView
from .models import Post
# Create your views here.


# CREATING A POST
#   queuing it
#   scheduling it
#   drafting it
class CreatePost(CreateView,LoginRequiredMixin):
    model = Post
    fields = ['post_type','title','text','image','video','gif','audio','tags','source','quote_text','post_when','scheduled_date']
    template_name = 'post/new_post.html'
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.op = self.request.user#adding the op as the one creating the post
        self.object.save()
        return super().form_valid(form)

#DASHBOARD
class Dashboard(ListView,LoginRequiredMixin):
    model = Post
    template_name = 'post\dashboard.html'
    paginate_by = 20
    context_object_name = 'posts'


# DELETING A POST

# EDITING A POST

# VIEW POST DETAILS


# REBLOGGING A POST


# LIKING A POST
#  https://www.youtube.com/watch?v=PXqRPqDjDgc
