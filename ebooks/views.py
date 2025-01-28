from django.shortcuts import render
from .models import  myBooks

# Create your views here.
def home(request):
    books=myBooks.objects.all()
    context={'books':books}
    return render (request, 'index.html', context)
