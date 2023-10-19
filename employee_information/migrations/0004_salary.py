# Generated by Django 4.1.7 on 2023-09-20 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0003_login_hours_active_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('basic_salary', models.FloatField()),
                ('HRA', models.FloatField()),
                ('medical_allowance', models.FloatField()),
                ('conveyance_allowance', models.FloatField()),
                ('leave_travel_allowance', models.FloatField()),
                ('special_allowance', models.FloatField()),
                ('pt_maharashtra', models.FloatField()),
                ('employee_share_in_pf', models.FloatField()),
                ('health_insurance', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employee_personal')),
            ],
        ),
    ]