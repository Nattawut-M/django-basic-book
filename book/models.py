from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories' # changed from 'Categorys' to 'Categories' (plural)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class LanguagesCoding(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    BOOK_LEVEL_CHOICES = [
        ('B', 'Basic'),
        ('M', 'Medium'),
        ('A', 'Advance')
    ]

    code = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    price = models.FloatField(default=0, null=False, blank=False)
    # Choice
    level = models.CharField('Level of Book', max_length=20, choices=BOOK_LEVEL_CHOICES, default=BOOK_LEVEL_CHOICES[0][1])
    # relationship
    languages = models.ForeignKey(LanguagesCoding, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    
    published = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Book'
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=1)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Book Comment'

    def __str__(self):
        return self.comment
    