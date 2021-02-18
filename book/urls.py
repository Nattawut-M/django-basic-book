from django.urls import path, re_path
# check premission to access path
from django.contrib.auth.decorators import login_required


from  . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('book_detail/<slug:slug>', login_required(views.book_detail, login_url='book:login'), name='book-detail'),
    re_path(r'^book_add/$', login_required(views.book_add, login_url='book:login'), name='book-add'), # login before access path
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup', views.signup_view, name = 'signup'),
]

