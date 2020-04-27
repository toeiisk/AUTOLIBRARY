import pytz
import datetime
from mylibrary.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required, permission_required

def search_book(request):
    context = {}
    search = request.GET.get('search', '') # get ค่าที่มาจาก search
    context['search'] = search #กำหนดค่าให้
    context['book'] = Book_info.objects.filter(name_book__icontains=search)
    #เอาค่า search มาเทียบกับ name ของ Restaurnt เพื่อนำมาแสดง
    return render(request, 'category/index.html', context=context)

def math(request):
    allbook = Book_info.objects.order_by('id')
    publisher = Publisher.objects.all()
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()

    return render (request, 'category/mathpage.html',
                    context = {
                        'allbook' : allbook,
                        'publisher' : publisher,
                        'booktype' : booktype,
                        'alltype' : alltype
                    }
                )

def science(request):
    allbook = Book_info.objects.all()
    publisher = Publisher.objects.all()
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()
    
    return render (request, 'category/sciencepage.html',
                    context = {
                        'allbook' : allbook,
                        'publisher' : publisher,
                        'booktype' : booktype,
                        'alltype' : alltype
                    }
                )
                
def blogbook(request, num):
    book = Book_info.objects.get(pk=num)
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()
    allbook = Book_info.objects.all()

    amout_book = book.amount_book

    return render (request, 'category/book.html',
                    context={
                        'book' : book,
                        'booktype' : booktype,
                        'alltype' : alltype,
                        'allbook' : allbook,
                        'amount_book' : amout_book
                    }
    )

def computer(request):
    count = 0
    datenow = datetime.now()
    computer = Computer.objects.all()
    datenow = pytz.utc.localize(datenow)
    datenow = datenow.replace(tzinfo=pytz.utc)
    for i in computer:
        if i.status_com == 'UNAVAILABLE':
            borrower_computer = Borrower_Computer.objects.filter(computer=i.id)
            # print('++++++++++++++++++++++++++++++', borrower_computer)
            if (borrower_computer[len(borrower_computer)-1].expire_date < datenow):
                i.status_com = 'AVAILABLE'
                i.save()
            print(borrower_computer[len(borrower_computer)-1].expire_date - datenow, '++++++++++')
        if i.status_com == 'AVAILABLE':
            count += 1
    return render (request, 'category/computerpage.html', 
                    context = {
                        'count' : count,
                        'computer' :computer
                    }
    )
    
def tutor(request):
    count = 0
    datenow = datetime.now()
    tutorroom = Tutor_room.objects.all()
    datenow = pytz.utc.localize(datenow)
    datenow = datenow.replace(tzinfo=pytz.utc)
    for i in tutorroom:
        if i.status_room == 'UNAVAILABLE':
            borrower_tutor_room = Borrower_Tutor_Room.objects.filter(tutor_room=i.id)
            if (borrower_tutor_room[len(borrower_tutor_room)-1].expire_date < datenow):
                i.status_room = 'AVAILABLE'
                i.save()
            print(borrower_tutor_room[len(borrower_tutor_room)-1].expire_date - datenow, '++++++++++')
        if i.status_room == 'AVAILABLE':
            count += 1
    return render (request, 'category/tutorpage.html', 
                    context = {
                        'tutorroom' : tutorroom,
                        'count' : count
                    }
    )

@login_required
@permission_required('mylibrary.delete_book_info')
def book_delete_math(request, num):
    if request.user.is_superuser:
        book = Book_info.objects.get(pk=num)
        book.delete()
        return redirect('math')
    else:
        return redirect('math')

@login_required
@permission_required('mylibrary.delete_book_info')
def book_delete_science(request, num):
    if request.user.is_superuser:
        book = Book_info.objects.get(pk=num)
        book.delete()
        return redirect('science')
    else:
        return redirect('science')