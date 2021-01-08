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
from .models import Post,Reblog,Note
# Create your views here.


# CREATING A POST
#   queuing it
#   scheduling it
#   drafting it
class CreatePost(CreateView,LoginRequiredMixin):
    model = Post
    fields = ['post_type','title','text','image','video','gif','audio','tags','source','quote_text','post_when','scheduled_date']
    template_name = 'post/new_post.html'
    success_url = reverse_lazy('dashboard')
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
        return reverse_lazy('post:detail',kwargs={'username':self.request.user.username,'pk':self.object.pk})






# LIKING A POST
def like(request,pk):
    post_to_be_liked = get_object_or_404(Post,id=request.POST.get('post_like'))
    post_to_be_liked.likes.add(request.user)
    next = request.POST.get('next','/')
    #adding to notes
    like_note = Note.objects.create(post=post_to_be_liked,user=request.user,note='LIKED')
    return HttpResponseRedirect(next)
#UNLIKING A POST
def unlike(request,pk):
    post_to_be_unliked = get_object_or_404(Post,id=request.POST.get('post_unlike'))
    post_to_be_unliked.likes.remove(request.user)
    next = request.POST.get('next','/')
    #removing from NOTES
    note_unlike = Note.objects.get(post=post_to_be_unliked,note='LIKED',user=request.user)
    note_unlike.delete()
    return HttpResponseRedirect(next)

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

# REBLOGGING A POST
class ReblogPost(CreateView,LoginRequiredMixin):
    model = Post
    fields = ['post_type','title','text','image','video','gif','audio','tags','source','quote_text','post_when','scheduled_date']
    template_name = 'post/reblog_post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.op = self.request.user#adding the op as the one creating the post
        self.object.is_reblogged = True
        parent_post = Post.objects.get(pk=self.kwargs['pk'])
        self.object.text = parent_post.text + '<hr>' + self.object.text
        self.object.image = parent_post.image
        self.object.save()
        self.object.reblogs.add(parent_post.op,through_defaults={'parent_post':parent_post})
        reblog_note = Note.objects.create(post=parent_post,user=self.request.user,note=self.object.text)
        self.object.save()
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        parent_post = Post.objects.get(pk=self.kwargs['pk'])
        context['parent_post'] = parent_post#adding the context so it can be displayed with the form
        return context
#ADDING NOTES TO A POST

class AddNote(CreateView,LoginRequiredMixin):
    model = Note
    fields = ['note']
    success_url = reverse_lazy('dashboard')
    template_name = 'post/add_note.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        post_to_add_note = Post.objects.get(pk=self.kwargs['pk'])
        self.object.post = post_to_add_note
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post_to_add_note = Post.objects.get(pk=self.kwargs['pk'])
        context['post'] = post_to_add_note #adding the context so it can be displayed with the form
        return context
#ALL NOTES FOR POST
class NotesList(ListView,LoginRequiredMixin):
    model = Note
    template_name = 'post/all_notes.html'
    context_object_name = 'post_notes'

    def get_queryset(self,**kwargs):
        post_notes = Note.objects.all().select_related('post').filter(post__pk__iexact=self.kwargs['pk'])
        return post_notes
