from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all()  # Fetching all posts from the database
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):  # Generic view to list posts
    model = Post # Specify the model to use
    template_name = 'blog/home.html'  # Specify your template name #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # Name of the context variable to use in the template
    ordering = ['-date_posted']
    paginate_by = 5  # Number of posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

        

class PostDetailView(DetailView):  # Generic view to display a single post
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):  # Generic view to create a new post
    model = Post
    fields = ['title', 'content']  # Fields to include in the form
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)  # Call the parent class's form_valid method


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect to home after deletion
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):  
    return render(request, 'blog/about.html', {'title': 'About'}) 
    

