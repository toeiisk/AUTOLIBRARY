from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

class Book_infoInline(admin.TabularInline):
    model = Book_info
    extra = 0

class Tutor_roomAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name_room', 'status_room']
    list_per_page = 15
    list_filter = ['status_room']
    search_fields = ['name_room']

class ComputerAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name_com', 'status_com']
    list_per_page = 15
    list_filter = ['status_com']
    search_fields = ['name_com']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']
    list_per_page = 15
    search_fields = ['name']

    inlines = [Book_infoInline]

class All_typeAdmin(admin.ModelAdmin):
    list_display = ['id' ,'all_type_name']
    list_per_page = 15
    search_fields = ['all_type_name']

class Book_typeAdmin(admin.ModelAdmin):
    list_display = ['id' ,'type_book', 'all_type_id']
    list_per_page = 15
    search_fields = ['type_book']

class Book_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'isbn', 'name_book', 'amount_book', 'published_id']
    list_per_page = 15
    list_filter = ['published_id']
    search_fields = ['name_book']

class Borrow_NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_isbn', 'date', 'return_date', 'borrow_user']
    list_per_page = 15
    search_fields = ['book_isbn']

class CalculateFinesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id' ,'borrow_user', 'date', 'charg', 'status_cal']
    list_per_page = 15
    search_fields = ['status_cal']

class Borrower_Tutor_RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrow_user', 'tutor_room', 'date', 'expire_date']
    list_per_page = 15
    list_filter = ['tutor_room']
    search_fields = ['tutor_room']

class Borrower_ComputerAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrow_user', 'computer', 'date', 'expire_date']
    list_per_page = 15
    list_filter = ['computer']
    search_fields = ['computer']

class IdcardAdmin(admin.ModelAdmin):
    list_display = ['user_idcard', 'idcard']
    list_per_page = 15
    search_fields = ['user_idcard']

# Register your models here.
admin.site.register(Permission)
admin.site.register(Tutor_room, Tutor_roomAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book_info, Book_infoAdmin)
admin.site.register(Borrow_Notes, Borrow_NotesAdmin)
admin.site.register(Borrower_Computer, Borrower_ComputerAdmin)
admin.site.register(Borrower_Tutor_Room, Borrower_Tutor_RoomAdmin)
admin.site.register(All_type, All_typeAdmin)
admin.site.register(Book_type, Book_typeAdmin)
admin.site.register(Idcard, IdcardAdmin)
admin.site.register(CalculateFines, CalculateFinesAdmin)
