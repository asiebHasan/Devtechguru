from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book

# Create your views here.


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "books/dashboard.html", {"books": books})


@login_required
def create_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        if title:
            Book.objects.create(title=title, description=description)
            messages.success(request, "Book added")
            return redirect("home")
        else:
            messages.error(request, "invalid title")
            return redirect("create_book")
    else:
        return render(request, "books/create.html")
