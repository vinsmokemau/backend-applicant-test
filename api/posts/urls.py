"""Posts' Urls."""

# DRF
from rest_framework import routers

# Posts App
from .viewsets import (
    PostViewSet,
    CommentViewSet,
)

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
