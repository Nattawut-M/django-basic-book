from django.contrib import admin
from book.models import *

# Admin Conf
class BookCommentStackInline(admin.StackedInline):
    model = BookComment
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'price', 'published']
    list_filter = ['published', 'category', 'author', 'languages']
    search_fields = ['name']
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ['name']} # auto add 'slug' from 'name
    inlines = [BookCommentStackInline] # class BookCommentStackInline
    

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(LanguagesCoding)