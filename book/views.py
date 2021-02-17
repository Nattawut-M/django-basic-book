from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage
# import Models
from .models import *

# Create your views here.
def index(request):
    book = Book.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')
    if  category_id:
        book = Book.objects.filter(category=category_id)

    book_paginator = Paginator(book, 3)
    book_page = request.GET.get('page')
    try:
        book = book_paginator.page(book_page)
    except PageNotAnInteger:
        book = book_paginator.page(1)
    except EmptyPage:
        # if ?page over than number of pages, then set page = last page of pagination
        book = book_paginator.page(book_paginator.num_pages)
    except InvalidPage:
        book = book_paginator.page(1)

    return render(request, 'book/index.html', {'book':book, 'categories': categories, 'category_id':category_id})
