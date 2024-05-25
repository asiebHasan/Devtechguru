from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('create', views.create_book, name='create_book'),
]
