# Generated by Django 4.1.7 on 2023-09-27 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0014_alter_login_hours_break_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login_Hours',
        ),
    ]
