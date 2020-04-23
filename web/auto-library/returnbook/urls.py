from django.urls import path
from . import views 

urlpatterns = [
    path('return-book/<int:num>/', views.return_book, name='return_book'),
    # path('return_book_last/', views.return_book_last, name='return_book_last'),

]