from django.urls import path
from . import views 

urlpatterns = [
    path('math/', views.math, name='math'),
    path('science/', views.science, name='science'),
    path('computer/', views.computer, name='computer'),
    path('tutor/', views.tutor, name='tutor'),
    path('book/<int:num>/', views.blogbook, name='blogbook'),
    path('search/', views.search_book, name="search_book"),
    path('book_info/<int:num>/delete/', views.book_delete_math, name='book_delete_math'),
    path('book_info/<int:num>/delete/', views.book_delete_science, name='book_delete_science'),
]