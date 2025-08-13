from django.urls import path, include
from . import views  
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('about/', views.about, name='blog_about'),    
    path('', PostListView.as_view() , name='blog_home'),
     path('user/<str:username>', UserPostListView.as_view() , name='user-posts'),  # List posts by a specific user
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view for a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create view for a new post
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),  # Delete view for a post
]

 






