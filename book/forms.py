from django.forms import ModelForm

from book.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        exclude = ['code', 'slug', 'created', 'updated']
