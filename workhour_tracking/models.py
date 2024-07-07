from django.db import models
from employee_records.models import Employee


class WorkHour(models.Model):
    SHIFT_CHOICES = [
        ('day', 'Day'),
        ('night', 'Night')
    ]

    HOUSE_CHOICES = [
        ('jericho', 'Jericho House'),
        ("howards", "Howard's House")
    ]

    start_date = models.DateField()
    end_date = models.DateField()
    staff_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, default=12)
    # hourly_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_wage = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    house = models.CharField(max_length=10, choices=HOUSE_CHOICES)

    def calculate_total_wage(self):
        return self.staff_name.hourly_rate * (self.total_hours + self.overtime_hours)

    def save(self, *args, **kwargs):
        self.total_wage = self.calculate_total_wage()
        super().save(*args, **kwargs)


class EmployeeAbsence(models.Model):
    ABSENCE_CHOICES = [
        ('sick', 'Sick Day'),
        ('holiday', 'Holiday'),
        ('personal', 'Personal')
    ]
    
    date = models.DateField()
    staff_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    why_absent = models.CharField(max_length=50, choices=ABSENCE_CHOICES)

    def __str__(self):
        return f"{self.staff_name} - {self.date} - {self.why_absent}"