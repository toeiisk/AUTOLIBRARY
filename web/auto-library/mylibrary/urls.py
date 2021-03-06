from django.urls import path
from django.conf.urls import url, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='my_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('checkbook/', views.checkbook, name='checkbook'),
    path('checkcom/', views.checkcom, name='checkcom'),
    path('checktutorroom/', views.checktutorroom, name='checktutorroom'),
    path('testapi/', views.testapi, name='testapi'),
]