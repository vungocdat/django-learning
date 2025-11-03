from django.urls import path
from . import views

urlpatterns = [
    # starting page /blog - in global urls.py it is set to /
    path("", views.starting_page, name="starting-page"),
    # /blog/posts
    path("posts", views.posts, name="posts-page"),
    # /blog/posts/dynamic_part (slug is universal placeholder)
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]
