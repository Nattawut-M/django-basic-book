from django.urls import path, re_path
from  . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('book_detail/<slug:slug>', views.book_detail, name='book-detail'),
    re_path(r'^book_add/$', views.book_add, name='book-add'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    
]

