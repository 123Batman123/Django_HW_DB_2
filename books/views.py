from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Book

def home_i(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('name')

    context = {
        'books': books,
    }
    return render(request, template, context)


def book_pub_date(request, date_pub):
    template = 'books/date_pub.html'
    books = Book.objects.all().order_by('pub_date')

    p_page = None
    n_page = None
    for i, book in enumerate(books):
        if date_pub.date() == book.pub_date:
            need_book = book
            index_b = i

    if index_b != 0:
        p_page = books[index_b - 1].pub_date
    if index_b != len(books) - 1:
        n_page = books[index_b + 1].pub_date
    print(p_page, n_page)

    context = {
        'book': need_book,
        'p_page': p_page,
        'n_page': n_page,
    }
    return render(request, template, context)
