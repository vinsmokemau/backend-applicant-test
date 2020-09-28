"""blog URL Configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('posts.urls')),
]
