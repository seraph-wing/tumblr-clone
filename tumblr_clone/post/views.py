from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,TemplateView,UpdateView,ListView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
#from braces.views import SelectRelatedMixin
User = get_user_model()
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

    def get_queryset(self):
        u =self.request.user
        following_users = u.is_followed_by.all()
        follow_posts = Post.objects.all().filter(op__in=following_users)
        return follow_posts
#VIEW POST DETAILS

class PostDetail(DetailView):
    model = Post
    template_name = 'post\detail.html'

# DELETING A POST

class PostDelete(DeleteView,LoginRequiredMixin):
    model = Post
    template_name = 'post\post_delete.html'
    success_url = reverse_lazy('dashboard')
    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)

# EDITING A POST
class EditPost(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['post_type','title','text','image','video','gif','audio','tags','source','quote_text']
    template_name = 'post\edit_post.html'
    slug_field = 'pk'

    def get_success_url(self,*args,**kwargs):
        return reverse_lazy('post:detail',kwargs={'username':User.username,'pk':self.object.pk})



# REBLOGGING A POST


# LIKING A POST
def like(request,pk):
    post_to_be_liked = get_object_or_404(Post,id=request.POST.get('post_like'))
    post_to_be_liked.likes.add(request.user)
    return HttpResponseRedirect(reverse('dashboard'))
#UNLIKING A POST
def unlike(request,pk):
    post_to_be_unliked = get_object_or_404(Post,id=request.POST.get('post_unlike'))
    post_to_be_unliked.likes.remove(request.user)
    return HttpResponseRedirect(reverse('dashboard'))

#  https://www.youtube.com/watch?v=PXqRPqDjDgc
#USER POSTS
class UserPosts(ListView,LoginRequiredMixin):
    model = Post
    template_name = 'post/user_post.html'
    paginate_by = 20
    context_object_name = 'user_posts'

    def get_queryset(self):
        self.username = get_object_or_404(User,username=self.kwargs['username'])
        all_posts = Post.objects.all().filter(op__exact=self.username)
        return all_posts
