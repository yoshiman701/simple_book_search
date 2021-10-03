from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Author,Book
import re

        
class IndexView(ListView):
    template_name = "search/index.html" 
    model = Author
   
class BookDetailView(DetailView):
    template_name = "search/book_detail.html"
    context_object_name = 'book_detail'
    model = Book
   
class SearchResultView(ListView):
    template_name = "search/book_list.html"
    model = Book
    
    def get_queryset(self):
        queryset = []
        
        if self.request.GET.get('title'):
            pattern = re.compile(r"^(?=.*" + re.escape(self.request.GET.getlist('title')[0]) +r").*$")
            [queryset.append(i) for i in Book.objects.all() if pattern.match(i.title)]          
            
        elif self.request.GET.get('author'):
            pattern = re.compile(r"^(?=.*" + re.escape(self.request.GET.getlist('author')[0]) +r").*$")
            [queryset.append(i) for i in Book.objects.all() if pattern.match(i.authors.all().first().name)]      
            
            
        elif self.request.GET.get('publisher'):
            pattern = re.compile(r"^(?=.*" + re.escape(self.request.GET.getlist('publisher')[0]) +r").*$")
            [queryset.append(i) for i in Book.objects.all() if pattern.match(i.publisher.all().first().name)]          
           
        else:
            queryset = []
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_list = {"book_list":self.get_queryset()}
        book_summary = []
        [book_summary.append(i.summary) for i in self.get_queryset()]       
        context['json_date'] = {'book_summary':book_summary}
        context.update(book_list)
        
        return context        
        
        
        
        
        
        
        
        
        
        
        
        
        

