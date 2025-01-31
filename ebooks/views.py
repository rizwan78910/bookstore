
from django.shortcuts import render, redirect, get_object_or_404
from .models import myBooks  # Ensure correct model name
from .forms import BookForm  # Create a form for book data

def home(request):
    books = myBooks.objects.all()  # Retrieve all books
    return render(request, 'index.html', {'books': books})  # Pass books to template

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def update_book(request, book_id):
    book = get_object_or_404(myBooks, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(myBooks, id=book_id)
    book.delete()
    return redirect('home')
