from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Tutor_room(models.Model):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    STATUS = [
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    ]
    
    name_room = models.CharField(max_length=250, default='SOME STRING')
    img_tutor = models.ImageField(upload_to='static/static_dirs/images/tutor/')
    status_room = models.CharField(max_length=12, choices=STATUS, default=AVAILABLE)
    
    class Meta:
        ordering=('name_room',)
        verbose_name='เพิ่มห้องติว'
        verbose_name_plural="ห้องติว"
    
    def __str__(self):
        return '(%s) %s' %(self.id, self.name_room) 

class Computer(models.Model):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    STATUS = [
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    ]

    name_com = models.CharField(max_length=250, default='SOME STRING')
    img_com = models.ImageField(upload_to='static/static_dirs/images/computer/', null=True)
    status_com = models.CharField(max_length=12, choices=STATUS, default=AVAILABLE)
    
    class Meta:
        ordering=('name_com',)
        verbose_name='เพิ่มคอมพิวเตอร์'
        verbose_name_plural="คอมพิวเตอร์"
    
    
    def __str__(self):
        return '(%s) %s' %(self.id, self.name_com) 

class Publisher(models.Model):
    name = models.CharField(max_length=250, default='SOME STRING')
    address = models.CharField(max_length=250, default='SOME STRING')
    def __str__(self):
        return '(%s) %s' %(self.id, self.name)
    class Meta:
        ordering=('name',)
        verbose_name='เพิ่มสำนักพิมพ์'
        verbose_name_plural="สำนักพิมพ์"

class All_type(models.Model):
    all_type_name = models.CharField(max_length=250)
    def __str__(self):
        return '(%s) %s' %(self.id, self.all_type_name)
    class Meta:
        ordering=('all_type_name',)
        verbose_name='เพิ่มประเภทของหนังสือ'
        verbose_name_plural="ประเภทของหนังสือ"

class Book_type(models.Model):
    type_book = models.CharField(max_length=250, default='SOME STRING', editable=True)
    all_type_id =  models.ForeignKey(All_type, on_delete=models.PROTECT, related_name='book_type')
    class Meta:
        ordering=('type_book',)
        verbose_name='เพิ่มประเภทย่อยของหนังสือ'
        verbose_name_plural="ประเภทย่อยของหนังสือ"
    
    def __str__(self):
        return self.type_book 

class Book_info(models.Model):
    isbn = models.CharField(max_length=250, default='SOME STRING')
    img_book = models.ImageField(upload_to='static/static_dirs/images/')
    book_type_id = models.ForeignKey(Book_type, on_delete=models.PROTECT)
    name_book = models.CharField(max_length=250)
    amount_book = models.IntegerField()
    location_book = models.CharField(max_length=250)
    descri_book = models.CharField(max_length=250)
    published_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        ordering=('name_book',)
        verbose_name='เพิ่มหนังสือ'
        verbose_name_plural="หนังสือทั้งหมด"
    
    def __str__(self):
        return '(%s) %s' %(self.id, self.name_book)

class Borrow_Notes(models.Model):
    book_isbn = models.ForeignKey(Book_info, on_delete=models.PROTECT)
    date = models.DateTimeField(default=datetime.now())
    return_date = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '(%s) %s' %(self.id, self.borrow_user)
    
    class Meta:
        verbose_name='เพิ่มบันทึกการยืมหนังสือ'
        verbose_name_plural="บันทึกการยืมหนังสือ"

class CalculateFines(models.Model):
    COMPLETE = 'COMPLETE'
    UNCOMPLETE = 'UNCOMPLETE'
    STATUS = [
        (COMPLETE, 'COMPLETE'),
        (UNCOMPLETE, 'UNCOMPLETE')
    ]
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    charg = models.IntegerField(default='1')
    borrow_user = models.ForeignKey(Borrow_Notes, null=True, on_delete=models.SET_NULL)
    status_cal = models.CharField(max_length=12, choices=STATUS, default=UNCOMPLETE)
    name_book =  models.CharField(max_length=250)

    class Meta:
        verbose_name='เพิ่มบันทึกค่าปรับ'
        verbose_name_plural="บันทึกค่าปรับ"
    
    def str(self):
        return '(%s) %s' %(self.id, self.user_id)
    
class Borrower_Tutor_Room(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor_room = models.ForeignKey(Tutor_room, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    expire_date = models.DateTimeField(default=datetime.now()+timedelta(minutes=15))
    
    class Meta:
        verbose_name='เพิ่มผู้ยืมห้องติวหนังสือ'
        verbose_name_plural="ผู้ที่ยืมห้องติวหนังสือ"

    def __str__(self):
        return '(%s) %s' %(self.id, self.borrow_user)

class Borrower_Computer(models.Model):
    borrow_user = models.ForeignKey(User , on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    expire_date = models.DateTimeField(default=datetime.now()+timedelta(minutes=15))
    
    class Meta:
        verbose_name='เพิ่มผู้ยืมคอมพิวเตอร์'
        verbose_name_plural="ผู้ที่ยืมคอมพิเตอร์"

    
    def __str__(self):
        return '(%s) %s' %(self.id, self.borrow_user)

class Idcard(models.Model):
    user_idcard = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    idcard = models.CharField(max_length=250)

    class Meta:
        verbose_name='เพิ่มรหัสบัตรประชาชนของ user'
        verbose_name_plural="รหัสบัตรประชาชนของ user"

    def __str__(self):
        return '(%s) %s' %(self.user_idcard, self.idcard)

