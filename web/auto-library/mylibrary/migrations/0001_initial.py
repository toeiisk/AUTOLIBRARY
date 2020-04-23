# Generated by Django 3.0.5 on 2020-04-23 12:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='All_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_type_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Book_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(default='SOME STRING', max_length=250)),
                ('img_book', models.ImageField(upload_to='static/static_dirs/images/')),
                ('name_book', models.CharField(max_length=250)),
                ('amount_book', models.IntegerField()),
                ('location_book', models.CharField(max_length=250)),
                ('descri_book', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('book_isbn', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mylibrary.Book_info')),
                ('borrow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_com', models.CharField(default='SOME STRING', max_length=250)),
                ('img_com', models.ImageField(upload_to='static/static_dirs/images/computer/')),
                ('status_com', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('UNAVAILABLE', 'UNAVAILABLE')], default='AVAILABLE', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Idcard',
            fields=[
                ('user_idcard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('idcard', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SOME STRING', max_length=250)),
                ('address', models.CharField(default='SOME STRING', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_room', models.CharField(default='SOME STRING', max_length=250)),
                ('img_tutor', models.ImageField(upload_to='static/static_dirs/images/tutor/')),
                ('status_room', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('UNAVAILABLE', 'UNAVAILABLE')], default='AVAILABLE', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='CalculateFines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('charg', models.IntegerField(default='1')),
                ('status_cal', models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('UNCOMPLETE', 'UNCOMPLETE')], default='UNCOMPLETE', max_length=12)),
                ('borrow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Borrow_Notes')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower_Tutor_Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 4, 23, 19, 4, 17, 895240))),
                ('expire_date', models.DateTimeField(default=datetime.datetime(2020, 4, 23, 19, 19, 17, 895240))),
                ('borrow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tutor_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Tutor_room')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower_Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 4, 23, 19, 4, 17, 896241))),
                ('expire_date', models.DateTimeField(default=datetime.datetime(2020, 4, 23, 19, 5, 17, 896241))),
                ('borrow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='Book_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_book', models.CharField(default='SOME STRING', max_length=250)),
                ('all_type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mylibrary.All_type')),
            ],
        ),
        migrations.AddField(
            model_name='book_info',
            name='book_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mylibrary.Book_type'),
        ),
        migrations.AddField(
            model_name='book_info',
            name='published_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Publisher'),
        ),
    ]