# management/commands/load_shift_data.py
from django.core.management.base import BaseCommand
from employee_records.models import Employee
from workhour_tracking.models import WorkHour
import pandas as pd
from datetime import datetime
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load shift data from pandas DataFrame into the SQLite database'

    def handle(self, *args, **kwargs):
    
        df = pd.read_csv('C:/Users/Ella/Desktop/wage_tracker/employee_records/fixtures/output.csv')


      
        for index, row in df.iterrows():
            try:
                try:
                    employee = Employee.objects.get(id=row['staff_name'])
                except Employee.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Employee with ID {row['staff_name']} does not exist"))
                    continue

                start_date = datetime.strptime(row['start_date'].split(' ')[0], '%Y-%m-%d').date()
                end_date = datetime.strptime(row['end_date'].split(' ')[0], '%Y-%m-%d').date()
                shift_start = datetime.strptime(row['shift_start'], '%H:%M:%S').time()
                shift_end = datetime.strptime(row['shift_end'], '%H:%M:%S').time()

                # Handle NaN values
                total_hours = Decimal(row['total_hours']) if not pd.isna(row['total_hours']) else Decimal('0.0')
                overtime_hours = Decimal(row['overtime_hours']) if not pd.isna(row['total_hours']) else Decimal('0.0')
                total_wage = Decimal(row['total_wage']) if not pd.isna(row['total_wage']) else Decimal('0.0')

              
              
                
                try:
                    work_hour = WorkHour.objects.get(start_date=start_date, end_date=end_date, staff_name=employee)
                    # Update existing record
                    work_hour.shift = row['shift']
                    work_hour.shift_start = shift_start
                    work_hour.shift_end = shift_end
                    work_hour.overtime_hours = row['overtime_hours']
                    work_hour.total_hours = row['total_hours']
                    work_hour.total_wage = row['total_wage']
                    work_hour.house = row['house']
                    work_hour.save()
                    self.stdout.write(self.style.SUCCESS(f'Updated WorkHour for {employee} on {start_date}'))
                except WorkHour.DoesNotExist:
                    # Create new WorkHour record
                    WorkHour.objects.create(
                    start_date=start_date,
                    end_date=end_date,
                    staff_name=employee,
                    shift=row['shift'],
                    shift_start=shift_start,
                    shift_end=shift_end,
                    overtime_hours=overtime_hours,
                    total_hours=total_hours,
                    total_wage=total_wage,
                    house=row['house']
                    )
                    self.stdout.write(self.style.SUCCESS(f'Created WorkHour for {employee} on {start_date}'))
                

                self.stdout.write(self.style.SUCCESS('Successfully loaded work hour data'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to load work hour data: {e}'))