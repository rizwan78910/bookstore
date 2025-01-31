from django import forms
from .models import myBooks

class BookForm(forms.ModelForm):
    class Meta:
        model = myBooks
        fields = ['title', 'author', 'genre', 'price', 'stock', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter author name'}),
            'genre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter book genre'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter book price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter stock count'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
