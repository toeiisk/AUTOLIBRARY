from datetime import date, datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import auth_logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from mylibrary.models import *


# Create your views here.
def index(request):
    book = Book_info.objects.all()
    return render(request, 'index.html', 
        context={ 
            'book': book,
        }
    )

def auth_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.POST.get('next_url')
            if next_url: 
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            error = "Username or Password Incorrect!!"
            context['username'] = username
            context['password'] = password
            context['error'] = "Username or Password Incorrect!!"
            return render(request, 'login.html', context)
        pass
    else:
        return render(request, 'login.html', context)

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

def my_logout(request):
    logout(request)
    return redirect('index')


def borrowed(request, num):
    user = request.user
    dateborrow = datetime.now()
    datereturn = datetime.now()+timedelta(days=7)
    book_user = Book_info.objects.get(pk=num)
    post = Borrow_Notes(book_isbn=book_user, date=dateborrow, return_date=datereturn  ,borrow_user=user)
    post.save()
    
    num = 1
    number = book_user.amount_book
    total =  number - num
    book_user.amount_book = total
    book_user.save()
    return redirect('dashboard')

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

# def check_login(request):
#     if request.method == "GET":
#         raise Http404("URL doesn't exitsts")
#     else:
#         response_data = {}
#         login = request.POST['username']
#         user = None
#         try:
#             try:
#                 user = User.objects.get(login = login)
#             except ObjectDoesNotExist as e:
#                 pass
#             except Exception as e:
#                 raise e
#             if not user:
#                 response_data["is_success"] = True
#             else:
#                 response_data["is_success"] = False
#         except Exception as e:
#             response_data["is_success"] = False
#             response_data["msg"] = "Some error."
        
#         return JsonResponse(response_data)

