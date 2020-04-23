from django.db import models
from django.contrib.auth.models import User


class Tuter_room(models.Model):
    status_room = models.CharField(max_length=250, default="", editable=True)


class Computer(models.Model):
    status_com = models.CharField(max_length=250, default="", editable=True)


class Borrow_Notes(models.Model):
    number_borrowed = models.IntegerField(" "),
    status_book = models.CharField(max_length=250, default="", editable=True),
    return_date = models.DateField((""), auto_now=False, auto_now_add=False)

class Book_info(models.Model):
    type_book = models.CharField(max_length=250, default="", editable=True),
    name_book = models.CharField(max_length=250, default="", editable=True),
    amount_book = models.IntegerField(("")),
    location_book = models.CharField(max_length=250, default="", editable=True),
    descri_book = models.CharField(max_length=250, default="", editable=True)

class CalculateFines(models.Model):
    date = models.DateField((""), auto_now=False, auto_now_add=False),
    chrage = models.IntegerField((""))