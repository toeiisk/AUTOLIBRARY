# Generated by Django 3.0.5 on 2020-04-24 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0003_auto_20200423_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 18, 5, 59, 13900)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 18, 20, 59, 13900)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 18, 5, 59, 13900)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 18, 20, 59, 13900)),
        ),
        migrations.AlterField(
            model_name='calculatefines',
            name='date',
            field=models.IntegerField(default='1'),
        ),
    ]
