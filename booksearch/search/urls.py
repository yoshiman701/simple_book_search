from django.urls import path
from . import views

app_name='search'
urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    
    path('search_result',views.SearchResultView.as_view(),name='search_result'),
]

