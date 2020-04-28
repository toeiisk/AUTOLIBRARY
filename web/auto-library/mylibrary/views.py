import json
from datetime import date, datetime, timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import auth_logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from mylibrary.models import *
from mylibrary.serializers import *
from .forms import UserLoginForm


# Create your views here.
def index(request):
    book = Book_info.objects.all()
    return render(request, 'index.html', 
        context={ 
            'book': book,
        }
    )

def user_login(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        next_url = request.POST.get('next_url')
        if next_url: 
            return redirect(next_url)
        else:
            return redirect('index')
    return render(request, 'login.html', {"form":form, "title":title})

def register(request):
    context = {}
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email')
            )
            group = Group.objects.get(name='User')
            user.groups.add(group)
            user = authenticate(request, username=username, password=password)
            if user:
                idcard_value = request.POST.get('idcard')
                idcard = Idcard.objects.filter(user_idcard=request.user.id)
                if not idcard:
                    print('Create IDCard')
                    idcard = Idcard(
                        user_idcard = user,
                        idcard = idcard_value,
                    )
                    idcard.save()
                    messages.success(request, 'Successfully registered and logged in')
                    return redirect('login')
                else:
                    idcard = idcard[0]
                    print(idcard.user_id, idcard)
                print(idcard, user)
        except Exception as e:           
            context['error'] = str(e)
    return render(request, 'register.html', context=context)

@login_required
def my_logout(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    user = request.user.id
    book = Borrow_Notes.objects.filter(borrow_user=user)
    firstname = request.user.first_name
    lastname = request.user.last_name
    useridcard = Idcard.objects.get(pk=user)
    username = request.user
    
    return render(request, 'dashboard.html',
        context={ 'firstname': firstname,
                  'lastname': lastname,
                  'useridcard': useridcard,
                  'book': book,
                  'username': username
        }
    )

@login_required
def checkbook(request):
    if request.user.is_superuser:
        history = CalculateFines.objects.all()
        return render(request, 'checkbook.html', context={'history' : history})
    else:
        messages.error(request, 'You not have permission!!!')
        return redirect('index')

@login_required
def checkcom(request):
    if request.user.is_superuser:
        checkcom = Borrower_Computer.objects.all()
        return render(request, 'checkcom.html', context={
            'checkcom' : checkcom,   
        })
    else:
        messages.error(request, 'You not have permission')
        return redirect('index')

@login_required
def checktutorroom(request):
    if request.user.is_superuser:
        checkroom = Borrower_Tutor_Room.objects.all()
        return render(request, 'checktutorroom.html', context={
            'checkroom' : checkroom
        })
    else:
        messages.error(request, 'You not have permission!!!')
        return redirect('index')


@csrf_exempt
def testapi(request):
    if request.method == 'GET':
        big_type = Computer.objects.all()
        serializer = ComputerSerializer(big_type, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ComputerSerializer(data=request.POST)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
