# Generated by Django 4.1.7 on 2023-09-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0004_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='employers_share_in_pf',
            field=models.FloatField(default=1584),
        ),
    ]