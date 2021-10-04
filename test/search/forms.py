from django import forms
from .models import Publisher,Author,Book

class BookForm(forms.ModelForm):
   
    class Meta:
        model = Book
        
        fields = ['title']
       
        


