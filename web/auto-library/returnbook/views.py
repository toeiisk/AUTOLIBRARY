
from .forms import *
from django.shortcuts import render, redirect

# Create your views here.
def return_book(request,num):
    returnbook = Borrow_Notes.objects.get(pk=num)
    calculatefine = CalculateFines.objects.filter(borrow_user=returnbook)
    
    # เช็คจำนวนหนังสือ
    check = Book_info.objects.get(pk=returnbook.book_isbn.id)
    for i in calculatefine:
        chek_date = i.date.date()
    
    datenow = datetime.now().date()
    Diff = (chek_date - datenow)
    count = ( Diff.days * 10)
    
    if count <= 0:
        for i in calculatefine:
            if i.status_cal == 'UNCOMPLETE':
                i.status_cal = 'COMPLETE'
                i.save()
        addbook = returnbook.book_isbn.amount_book
        result = addbook + 1
        check.amount_book = result
        check.save()
        returnbook.delete()
        return render(request, 'payment-complete.html', context={
            'calculatefine' : calculatefine
        })
    else:
        for i in calculatefine:
            i.charg = count
            i.save()
        addbook = returnbook.book_isbn.amount_book
        result = addbook + 1
        check.amount_book = result
        check.save()
        returnbook.delete()
        return render(request, 'payment-complete.html', context={
            'calculatefine' : calculatefine
        })

    # if count > 0:
    #     if len(postreturn) == 0:
    #         postreturn = CalculateFines(date=datenow,  borrow_user=returnbook, user_id=user, charg=count)
    #         postreturn.status_cal = 'COMPLETE'
    #         postreturn.save()
        
    #     get_return = return_book_last1(returnbook)
    #     context = {
    #         'get_return' : get_return,
    #     }  
    #     return render(request, 'payment.html', context=context)
    # else:
    #     postreturn = CalculateFines(date=datenow,  borrow_user=returnbook, user_id=user, charg=0)
    #     postreturn.status_cal = 'COMPLETE'
    #     postreturn.save()

    #     rate = 0
    #     checkpay = 0      
    #     cal = returnbook.book_isbn.amount_book
    #     result = cal + 1
    #     check.amount_book = result
    #     check.save()
    #     returnbook.delete()
# def payment(request):
    
#     return render(request, 'payment.html', context={})

def payment_complete(request, num):
    result =  CalculateFines.objects.filter(pk=num).values()
    datenow = datetime.now().date()
    checkpay = 1
    for i in result:
        # ดึง id ของ user ใน Model Calculate
        test = i['borrow_user_id'] 

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
        'result' : result,
        'checkpay' : checkpay,
        'rate_date' : rate_date
    })
