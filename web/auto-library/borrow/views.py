from fnmatch import filter
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from mylibrary.models import *

from .forms import *


# Create your views here.
def borrow_book(request,num):
    book = Book_info.objects.get(pk=num)
    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form,
        'book': book
    })

@login_required
def borrow_com(request, num):
    computer_id = Computer.objects.get(pk=num)
    user = request.user
    if request.method == 'POST':
        status = False
        form = BorrowComForm(request.POST)
        borrower_com = Borrower_Computer.objects.filter(borrow_user=user)

        if (borrower_com):
            com = Computer.objects.get(pk=borrower_com[len(borrower_com)-1].computer.id)
            if com.status_com == 'UNAVAILABLE':
                messages.error(request, 'คุณมีเครื่องที่ยังยืมอยู่')
            else:
                status = True
        else:
            status = True

        if status:
            if form.is_valid():            
                date = form.cleaned_data['date']
                expire_date = form.cleaned_data['expire_date']
                post = Borrower_Computer(
                    computer = computer_id, 
                    borrow_user = user,
                    date = date,
                    expire_date = expire_date
                )
                post.save()
            computer_id.status_com = 'UNAVAILABLE'
            computer_id.save()

            messages.success(request, 'Computer Booking is complete :)')
        return redirect('computer')

    borrow_form = BorrowComForm()

    return render(request, 'borrow-com.html', context={
        'form': borrow_form,
        'computer': computer_id,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'expire_date': (datetime.now()+timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    })

@login_required
def borrow_tutor(request, num):
    tutorroom_id = Tutor_room.objects.get(pk=num)
    user = request.user
    if request.method == 'POST':
        status = False
        form = BorrowTutorForm(request.POST)
        borrower_tutor_room = Borrower_Tutor_Room.objects.filter(borrow_user=user)
        if (borrower_tutor_room):
            tutor_room = Tutor_room.objects.get(pk=borrower_tutor_room[len(borrower_tutor_room)-1].tutor_room.id)
            if tutor_room.status_room == 'UNAVAILABLE':
                messages.error(request, 'คุณมีห้องที่จองค้างไว้อยู๋!!!')
            else:
                status = True
        else:
            status = True

        if status:
            if form.is_valid():            
                date = form.cleaned_data['date']
                expire_date = form.cleaned_data['expire_date']
                post = Borrower_Tutor_Room(
                    tutor_room = tutorroom_id, 
                    borrow_user = user,
                    date = date,
                    expire_date = expire_date
                )
                post.save()
            tutorroom_id.status_room = 'UNAVAILABLE'
            tutorroom_id.save()

            messages.success(request, 'Room Booking is complete :)')
        return redirect('tutor')

    borrow_form = BorrowTutorForm()

    return render(request, 'borrow-tutor.html', context={
        'form': borrow_form,
        'tutorroom': tutorroom_id,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'expire_date': (datetime.now()+timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    })
