from decimal import Decimal
from django.db import models
from admin_user.models import Admin_User
import re

# --------------------------------------------------------------------------

class EmployeeNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        kwargs['primary_key'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def generate_emp_number(self):
        emp_number = Admin_User.objects.order_by(
            '-id').first()
        print(emp_number)



        if emp_number:
            last_numeric_part = re.search(r'\d+$', emp_number.id)
            if last_numeric_part:
                last_numeric_value = int(last_numeric_part.group())
                
                new_emp_number= last_numeric_value + 1
            else:
                new_emp_number = 1
            
        else:
            new_emp_number = 1
        new_invoice_number_with_zeros = str(new_emp_number).zfill(3)
        print(new_invoice_number_with_zeros)
        return f"JTA{new_invoice_number_with_zeros}"

    def pre_save(self, model_instance, add):
        if not model_instance.id:
            model_instance.id = self.generate_emp_number()
        return super().pre_save(model_instance, add)
    
# -------------------------------------------------------------------------------------------

class Employee(models.Model):
    EMPLOYMENT_CHOICES = [
        ('permanent', 'Permanent'),
        ('bank', 'Bank')
    ]
    JOB_TITLE_CHOICES = [
        ('team_leader', 'Team Leader'),
        ('rcw', 'RCW'),
        ('srcw', 'SRCW'),
    ]
    HOURLY_RATE_CHOICES = [
    (Decimal('15.50'), 15.50),
    (Decimal('13.50'), 13.50),
    (Decimal('12.50'), 12.50)
    ]
    id = EmployeeNumberField()
    # first_name = models.CharField(max_length=100, default='empty')
    # last_name = models.CharField(max_length=100, default='name')
    staff_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=20, choices=JOB_TITLE_CHOICES)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2, choices=HOURLY_RATE_CHOICES)

    def __str__(self):
        return self.staff_name
