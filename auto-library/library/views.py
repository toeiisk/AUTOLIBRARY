from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import auth_logout
# Create your views here.
def index(request):

    return render (request, 'index.html')

def auth_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = "Username or Password Incorrect!!"
            context['username'] = username
            context['password'] = password
            context['error'] = "Username or Password Incorrect!!"
            return render(request, 'restaurant_home/login.html', context)
        pass
    else:
        return render(request, 'login.html', context)