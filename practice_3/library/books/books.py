from books.models import Book
from django.shortcuts import render


def get_all(request):
    books = get_all_books()
    return render(request, "books.html", {'books': books})


def get_one(request, book_id):
    book = get_one_book(book_id)
    return render(request, "book.html", {'book': book})


def get_all_books():
    return Book.objects.all()


def get_one_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
    except :
        return "Constraint error"
    return book
