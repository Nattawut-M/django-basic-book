from django.shortcuts import render
# import Models
from .models import *

# Create your views here.
def index(request):
    book = Book.objects.all()
    return render(request, 'book/index.html', {'book':book})
