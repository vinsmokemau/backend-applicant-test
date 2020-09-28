"""Posts' Models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title


class Post(models.Model):
    """."""

    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    published_date = models.DateField()
    is_active = models.BooleanField(default=False)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class Comment(models.Model):

    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        related_name='comments',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    comment = models.TextField()
    send_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-send_date']

    def __str__(self):
        return f'Comment: {self.title} of {self.user.get_full_name}'
