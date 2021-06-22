# Generated by Django 3.2.4 on 2021-06-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField()),
                ('working_hours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punch_in', models.TimeField()),
                ('punch_out', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employeemodel')),
            ],
        ),
    ]
