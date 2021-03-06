# Generated by Django 3.0.5 on 2020-04-25 09:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylibrary', '0008_auto_20200425_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 16, 34, 13, 886139)),
        ),
        migrations.AlterField(
            model_name='borrow_notes',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 16, 34, 13, 886139)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 16, 34, 13, 888139)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 16, 49, 13, 888139)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 16, 34, 13, 887139)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 16, 49, 13, 887139)),
        ),
        migrations.AlterField(
            model_name='calculatefines',
            name='borrow_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mylibrary.Borrow_Notes'),
        ),
        migrations.AlterField(
            model_name='calculatefines',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
