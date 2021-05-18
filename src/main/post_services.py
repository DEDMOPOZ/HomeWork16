from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .models import Post


def post_all():
    key = Post().__class__.cache_key()
    if key in cache:
        all_posts = cache.get(key)
    else:
        all_posts = Post.objects.all()
        cache.set(key, all_posts, 30 * 60)
    return all_posts


def post_find(post_id: int) -> Post:
    post = get_object_or_404(Post, pk=post_id)
    return post
