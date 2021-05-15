from django.core.cache import cache

from .models import Category


def categories():
    key = Category().__class__.cache_key()
    if key in cache:
        all_categories = cache.get(key)
    else:
        all_categories = Category.objects.all()
        cache.set(key, all_categories, 30 * 60)
    return all_categories
