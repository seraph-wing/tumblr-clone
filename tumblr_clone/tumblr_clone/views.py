from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from post.models import Post
from account.models import User
from django.db.models import Q
from functools import reduce
import operator

class LoginPage(TemplateView):
    template_name = 'login.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

"""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)
"""
class SearchPage(ListView):
    model = Post
    template_name = 'search_results.html'
    paginate_by = 50
    context_object_name = 'results'

    def get_queryset(self):
        users = User.objects.all()
        print(users)
        query = self.request.GET.get('query')

        if query:
            print(query)
                #users = users.filter(Q(username__contains=query) | Q(slug__icontains=query))
            query_list = query.split()
            posts = Post.objects.all().filter(reduce(operator.or_,
                   (Q(title__icontains=q) for q in query_list)) |
            reduce(operator.or_,
                   (Q(text__icontains=q) for q in query_list)) |
            reduce(operator.or_,
                   (Q(op__username__icontains=q) for q in query_list)) |
            reduce(operator.or_,
                   (Q(tags__name__icontains=q) for q in query_list))).distinct()
        #result = users | posts
        return posts

        def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            posts = Post.objects.all()
            query = self.request.GET.get('query')
            print(query)
            print(Post.objects.all())
            query_list = query.split()
            print(posts)
            print(query_list)
            posts = posts.filter(
                reduce(operator.or_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(text__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(op__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(tags__name__icontains=q) for q in query_list)))
            context['post_results'] = posts
            return context
