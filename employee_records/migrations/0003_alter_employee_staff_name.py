# Generated by Django 5.0.6 on 2024-07-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_records', '0002_employee_first_name_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='staff_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
