from django.core.cache import cache
from faker import Faker

from .models import Author


def authors():
    key = Author().__class__.cache_key()
    if key in cache:
        all_authors = cache.get(key)
    else:
        all_authors = Author.objects.all()
        cache.set(key, all_authors, 30 * 60)
    return all_authors


def new_author():
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return


def delete_all_authors():
    Author.objects.all().delete()
    return
