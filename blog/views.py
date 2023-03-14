from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializer
from property_andalucia_api.permissions import (
    IsSeller,
)


class BlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsSeller]
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
