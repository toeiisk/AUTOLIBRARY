# Generated by Django 3.0.5 on 2020-04-26 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0023_auto_20200426_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 0, 45, 11, 150283)),
        ),
        migrations.AlterField(
            model_name='borrow_notes',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 0, 45, 11, 150283)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 0, 45, 11, 156285)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 1, 0, 11, 156285)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 0, 45, 11, 154286)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 1, 0, 11, 154286)),
        ),
    ]
