"""Posts' Serializers."""

# DRF
from rest_framework import serializers

# Posts' Models
from .models import (
    Post,
    Comment
)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'published_date',
            'is_active',
            'content',
            'tags',
        ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'user',
            'post',
            'title',
            'comment',
            'send_date',
        ]
