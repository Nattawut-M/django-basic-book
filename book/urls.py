from django.urls import path, re_path
from  . import views
urlpatterns = [
    path('', views.index, name="home"),
    re_path(r'^book_add/$', views.book_add, name='book-add'),

]

