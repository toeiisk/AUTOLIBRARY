# Generated by Django 3.0.5 on 2020-04-26 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0020_auto_20200426_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 21, 55, 4, 751424)),
        ),
        migrations.AlterField(
            model_name='borrow_notes',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 21, 55, 4, 751424)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 21, 55, 4, 756423)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 22, 10, 4, 756423)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 21, 55, 4, 754422)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 22, 10, 4, 754422)),
        ),
    ]
