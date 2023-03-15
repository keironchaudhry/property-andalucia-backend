from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [
    path(
        'blog/',
        BlogListView().as_view()
    ),
    path(
        'blog/create/',
        BlogCreateView().as_view()
    ),
    path(
        'blog/<int:pk>/',
        BlogDetailView().as_view()
    ),
]
