from django.urls import path
from . import views 

urlpatterns = [
    path('borrow-book/<int:num>/', views.borrow_book, name='borrow_book'),
    path('borrow-com/<int:num>/', views.borrow_com, name='borrow_com'),
    path('borrow-tutor/<int:num>/', views.borrow_tutor, name='borrow_tutor'),
]