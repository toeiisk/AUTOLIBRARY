
from .forms import *
from django.shortcuts import render, redirect

# Create your views here.
def return_book(request,num):
    returnbook = Borrow_Notes.objects.get(pk=num)
    return_form = ReturnBookForm()
    datenow = datetime.now().date()
    datereturn = returnbook.return_date.date()
    user = request.user
    # Diff = (datenow - datereturn)
    Diff = (datereturn - datenow)
    count = (Diff.days*10)
    postreturn = CalculateFines.objects.filter(borrow_user=returnbook)
    # เช็คจำนวนหนังสือ
    check = Book_info.objects.get(pk=returnbook.book_isbn.id)

    if count > 0:
        if len(postreturn) == 0:
            postreturn = CalculateFines(date=datenow,  borrow_user=returnbook, user_id=user, charg=count)
            postreturn.save()

        cal = returnbook.book_isbn.amount_book
        result = cal + 1
        check.amount_book = result
        check.save()
        
        get_return = return_book_last1(returnbook)
        context = {
            'get_return' : get_return
        }
        
        return render(request, 'payment.html', context=context)
    else:
        postreturn = CalculateFines(date=datenow,  borrow_user=returnbook, user_id=user, charg=0)
        postreturn.save()
        rate = 0        
        cal = returnbook.book_isbn.amount_book
        result = cal + 1
        check.amount_book = result
        check.save()
        returnbook.delete()
        return render(request, 'payment-complete.html', context={
            'rate' : rate,
            'postreturn' : postreturn,

        })

def return_book_last1(returnbook):
    calculate = CalculateFines.objects.filter(borrow_user=returnbook)
    return calculate

def payment(request):
    
    return render(request, 'payment.html', context={})

def payment_complete(request):
    
    return render(request, 'payment-complete.html', context={})
