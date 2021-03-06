import datetime
import json
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from mylibrary.models import *
from .forms import *


# Create your views here.
@login_required
@permission_required('mylibrary.add_borrow_notes')
@permission_required('mylibrary.view_borrow_notes')
def borrow_book(request, num):
    book = Book_info.objects.get(pk=num)
    user = request.user
    if request.method == 'POST':
        form = BorrowNotesForm(request.POST)
        if form.is_valid():            
            date = form.cleaned_data['date']
            return_date = form.cleaned_data['return_date']
            #ดึงข้อมูลจากฟอร์ม เพื่อเอามาบันทึกใน Borrow_note
            post = Borrow_Notes(
                book_isbn = book, 
                borrow_user = user,
                date = date,
                return_date = return_date
            )
            post.save()

        num = 1 #เพื่อเอาไปลบกับหนังสือทั้งหมดใน catagory
        number = book.amount_book  #ดึงจำนวนหนังสือ
        total =  number - num
        book.amount_book = total #ลดจำนวนหนังสือเมื่อยืม
        book.save()

        date_return = post.return_date
        user_book_note = post
        #นำไปบันทึกใน Calculatefines เพื่อใช้คิดกรณีว่าเกินหรือไม่เกินวันที่คืน
        postreturn = CalculateFines(date=date_return, borrow_user=user_book_note, user_id=user, charg=0, name_book= book.name_book)
        postreturn.status_cal = 'UNCOMPLETE'
        postreturn.save()
        return redirect('dashboard')

    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form,
        'book': book
    })

@login_required
@permission_required('mylibrary.add_borrower_computer')
@permission_required('mylibrary.view_borrower_computer')
def borrow_com(request, num):
    computer_id = Computer.objects.get(pk=num)
    user = request.user
    if request.method == 'POST':
        status = False 
        form = BorrowComForm(request.POST)
        borrower_com = Borrower_Computer.objects.filter(borrow_user=user)

        if (borrower_com): #check ว่ามี user นี้ใน Borrow com ไหม
            com = Computer.objects.get(pk=borrower_com[len(borrower_com)-1].computer.id) #ดึง borrow_com อันล่าสุดและไปดึงไอดีของคอม
            if com.status_com == 'UNAVAILABLE': #check status ของ com 
                messages.info(request, 'คุณมีเครื่องที่ยังยืมอยู่') #แจ้งเตือนไปยังหน้ายืม
            else:
                status = True #ถ้าสถานะว่าง AVAILABLE เข้า if ล่าง
        else:
            status = True #ถ้าไม่มี เข้า if ล่าง

        if status:
            if form.is_valid(): #เช็คฟอร์มที่ส่งมา
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
            computer_id.save() #เปลี่ยนสถานะคอมเป็นไม่ว่าง
            code ='%x' % random.getrandbits(2 * 12) # random code เพื่อส่งยืนยันไปที่เมล
            
            send_mail(
                     'AUTO-LIBRARY รหัสยืนยันการจองคอมพิวเตอร์',
                     'โปรดกรอกรหัสนี้เพื่อเข้าใช้คอมพิวเตอร์ : %s' %code,
                     'emailtestlibrary@gmail.com',
                     [user.email]
                )   
            messages.success(request, 'Computer Booking is complete :)')
        return redirect('computer')

    borrow_form = BorrowComForm()

    return render(request, 'borrow-com.html', context={
        'form': borrow_form,
        'computer': computer_id,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #เปลี่ยน format เวลา
        'expire_date': (datetime.now()+timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S") #เปลี่ยน format เวลา
    })

@login_required
@permission_required('mylibrary.add_borrower_tutor_room')
@permission_required('mylibrary.view_borrower_tutor_room')
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
            code ='%x' % random.getrandbits(2 * 12)
            send_mail(
                     'AUTO-LIBRARY รหัสยืนยันการจองห้องติว',
                     'โปรดกรอกรหัสนี้เพื่อเข้าใช้ห้องติว : %s' %code,
                     'emailtestlibrary@gmail.com',
                     [user.email]
                )  
            messages.success(request, 'Room Booking is complete :)')
        return redirect('tutor')

    borrow_form = BorrowTutorForm()

    return render(request, 'borrow-tutor.html', context={
        'form': borrow_form,
        'tutorroom': tutorroom_id,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'expire_date': (datetime.now()+timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S")
    })
