# Generated by Django 3.0.5 on 2020-04-25 10:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylibrary', '0015_auto_20200425_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 53, 46, 149389)),
        ),
        migrations.AlterField(
            model_name='borrow_notes',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 17, 53, 46, 149389)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 53, 46, 150390)),
        ),
        migrations.AlterField(
            model_name='borrower_computer',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 18, 8, 46, 150390)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 53, 46, 150390)),
        ),
        migrations.AlterField(
            model_name='borrower_tutor_room',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 18, 8, 46, 150390)),
        ),
        migrations.CreateModel(
            name='CalculateFines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('charg', models.IntegerField(default='1')),
                ('status_cal', models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('UNCOMPLETE', 'UNCOMPLETE')], default='UNCOMPLETE', max_length=12)),
                ('borrow_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylibrary.Borrow_Notes')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
