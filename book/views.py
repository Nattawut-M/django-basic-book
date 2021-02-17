from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# import Paginator
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage
# import Models
from .models import *
# import Forms
from .forms import *
#import python-slugify
from slugify import slugify
# import messages
from django.contrib import messages

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

def book_add(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            book = form.save(commit=0) # insert data to form, but not commit 
            book.code = Book.objects.all().count() +1
            book.slug = slugify(book.name)
            book.save()
            form.save(commit=1)
            form.save_m2m()
            messages.success(request=request, message="Add New Book Success")
            return HttpResponseRedirect(reverse('book:home',kwargs={}))
        messages.error(request, 'Something went Wrongs !!')
        
    return render(request, 'book/book_add.html', {'form':form})

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book/book_detail.html', {'slug':slug, 'book':book})