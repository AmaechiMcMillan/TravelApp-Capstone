# Generated by Django 3.2.7 on 2021-09-28 05:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0007_auto_20210927_2126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='leave_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 5, 3, 30, 342910)),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 5, 3, 30, 342921)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 5, 3, 30, 341907)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 5, 3, 30, 341926)),
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('is_email', models.BooleanField(default=False)),
                ('is_password', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
