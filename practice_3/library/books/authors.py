from books.models import Authors
from django.shortcuts import render


def get_all(request):
    authors = get_all_authors()
    return render(request, "authors.html", {'authors': authors})


def get_one(request, author_id):
    author = get_one_author(author_id)
    return render(request, "author.html", {'author': author})


def get_all_authors():
    return Authors.objects.all()


def get_one_author(author_id):
    try:
        author = Authors.objects.get(id=author_id)
    except:
        return "Constraint error"
    return author
