# Generated by Django 5.0.6 on 2024-07-03 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('shift', models.CharField(choices=[('day', 'Day'), ('night', 'Night')], max_length=10)),
                ('shift_start', models.TimeField()),
                ('shift_end', models.TimeField()),
                ('overtime_hours', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('total_hours', models.DecimalField(decimal_places=2, default=12, max_digits=5)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_wage', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('house', models.CharField(choices=[('jericho', 'Jericho House'), ('howards', "Howard's House")], max_length=10)),
                ('staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_records.employee')),
            ],
        ),
    ]
