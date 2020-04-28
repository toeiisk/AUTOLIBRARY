
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('mylibrary.view_calculatefines')
# Create your views here.
def return_book(request,num):
    returnbook = Borrow_Notes.objects.get(pk=num)
    calculatefine = CalculateFines.objects.filter(borrow_user=returnbook)
    
    # เช็คจำนวนหนังสือ
    check = Book_info.objects.get(pk=returnbook.book_isbn.id)
    for i in calculatefine:
        chek_date = i.date.date()
    
    datenow = datetime.now().date()
    # วันที่คืน - วันปัจจุบัน
    Diff = (chek_date - datenow)
    # Diff = (datenow - chek_date)
    count = ( Diff.days * 10)
    rate = Diff.days
    paycheck = 1
    
    if count <= 0:
        for i in calculatefine:
            rate = 0
            if i.status_cal == 'UNCOMPLETE':
                i.status_cal = 'COMPLETE'
                i.save()
        addbook = returnbook.book_isbn.amount_book
        result = addbook + 1
        check.amount_book = result
        check.save()
        returnbook.delete()

        return render(request, 'payment-complete.html', context={
            'calculatefine' : calculatefine,
            'rate' : rate,
            'paycheck' : paycheck
        })
    else:
        for i in calculatefine:
            i.charg = count
            i.save()
        return render(request, 'payment.html', context={
            'calculatefine' : calculatefine,
            'rate' : rate
        })

@login_required
@permission_required('mylibrary.view_calculatefines')
def payment_complete(request, num):
    
    result =  CalculateFines.objects.filter(pk=num).values()
    updatecalculate =  CalculateFines.objects.get(pk=num)
    checkpay = 2
    datenow = datetime.now().date()
    
    
    for i in result:
        # ดึง id ของ user ใน Model Calculate
        test = i['borrow_user_id'] 
    
    updatecalculate.status_cal = 'COMPLETE'
    updatecalculate.save()
    


    note_borrow = Borrow_Notes.objects.get(pk=test)
    check = Book_info.objects.get(pk=note_borrow.book_isbn.id)    
    return_date = note_borrow.return_date.date()
    calculate_rate_date = datenow - return_date
    
    rate_date = -(calculate_rate_date.days)
    cal = note_borrow.book_isbn.amount_book
    addbook = cal + 1
    check.amount_book = addbook
    check.save()
    
    checkpay = 1
    note_borrow.delete()
    return render(request, 'payment-complete.html', context={
        'rate_date' : rate_date,
        'result' : result,
        'checkpay' : checkpay
    })
