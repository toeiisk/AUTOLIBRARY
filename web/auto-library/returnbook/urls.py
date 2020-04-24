from django.urls import path
from . import views 

urlpatterns = [
    path('return-book/<int:num>/', views.return_book, name='return_book'),
    path('payment', views.payment, name='payment'),
    path('payment-complete<int:num>', views.payment_complete, name='payment-complete'),
    # path('return_book_last/', views.return_book_last, name='return_book_last'),

]