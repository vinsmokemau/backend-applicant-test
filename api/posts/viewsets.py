"""Posts' Viewsets."""

# DRF
from rest_framework import viewsets

# Posts App
from .models import (
    Post,
    Comment
)
from .serializers import (
    PostSerializer,
    CommentSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """General ViewSet for Posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """General ViewSet for Comments."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
