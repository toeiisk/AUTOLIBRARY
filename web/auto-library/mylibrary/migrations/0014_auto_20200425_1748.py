# Generated by Django 3.0.5 on 2020-04-25 10:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylibrary', '0013_auto_20200425_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 48, 13, 458203)),
        ),
        migrations.AlterField(
            model_name='borrow_notes',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 17, 48, 13, 458203)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 48, 13, 460203)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 18, 3, 13, 460203)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 48, 13, 459203)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 18, 3, 13, 459203)),
        ),
        migrations.AlterField(
            model_name='calculatefines',
            name='borrow_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylibrary.Borrow_Notes'),
        ),
        migrations.AlterField(
            model_name='calculatefines',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
