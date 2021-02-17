from django.shortcuts import render
# import Models
from .models import *

# Create your views here.
def index(request):
    book = Book.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')
    if  category_id:
        book = Book.objects.filter(category=category_id)
    return render(request, 'book/index.html', {'book':book, 'categories': categories, 'category_id':category_id})
