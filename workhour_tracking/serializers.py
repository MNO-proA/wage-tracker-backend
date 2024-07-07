from rest_framework import serializers
from .models import WorkHour
from .models import EmployeeAbsence
from datetime import datetime


class WorkHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHour
        fields = ['id', 'start_date', 'end_date', 'staff_name', 'shift', 'shift_start', 'shift_end', 'overtime_hours', 'total_hours', 'total_wage', 'house']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['start_date'] = instance.start_date.strftime('%Y-%m-%d')
        representation['end_date'] = instance.end_date.strftime('%Y-%m-%d')
        representation['shift_start'] = instance.shift_start.strftime('%H:%M:%S')
        representation['shift_end'] = instance.shift_end.strftime('%H:%M:%S')
        return representation

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def create(self, validated_data):
        start_date = validated_data['start_date']
        start_date_str = start_date.strftime('%Y-%m-%d')
        validated_data['start_date'] = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        
        end_date = validated_data['end_date']
        end_date_str = end_date.strftime('%Y-%m-%d')
        validated_data['end_date'] = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        
        shift_start = validated_data['shift_start']
        shift_start_str = shift_start.strftime('%H:%M:%S')
        validated_data['shift_start'] = datetime.strptime(shift_start_str, '%H:%M:%S').time()

        shift_end = validated_data['shift_end']
        shift_end_str = shift_end.strftime('%H:%M:%S')
        validated_data['shift_end'] = datetime.strptime(shift_end_str, '%H:%M:%S').time()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        start_date = validated_data['start_date']
        start_date_str = start_date.strftime('%Y-%m-%d')
        validated_data['start_date'] = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        
        end_date = validated_data['end_date']
        end_date_str = end_date.strftime('%Y-%m-%d')
        validated_data['end_date'] = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        
        shift_start = validated_data['shift_start']
        shift_start_str = shift_start.strftime('%H:%M:%S')
        validated_data['shift_start'] = datetime.strptime(shift_start_str, '%H:%M:%S').time()

        shift_end = validated_data['shift_end']
        shift_end_str = shift_end.strftime('%H:%M:%S')
        validated_data['shift_end'] = datetime.strptime(shift_end_str, '%H:%M:%S').time()
        return super().update(instance, validated_data)
    
    
    
# serializers.py


class EmployeeAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAbsence
        fields = ['id', 'date', 'staff_name', 'why_absent']

    def to_representation(self, instance):
        representation = super().to_representation(instance)  
        # Format date as YYYY-MM-DD for HTML input and JS
        representation['date'] = instance.date.isoformat()
        return representation

    def to_internal_value(self, data):
        date_str = data.get('date')
        if date_str:
            try:
                # Try parsing as YYYY-MM-DD (HTML date input format)
                parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                try:
                    # Try parsing as MM/DD/YYYY (common US format)
                    parsed_date = datetime.strptime(date_str, '%m/%d/%Y').date()
                except ValueError:
                    raise serializers.ValidationError({'date': 'Invalid date format. Use YYYY-MM-DD or MM/DD/YYYY.'})
            
            data['date'] = parsed_date

        return super().to_internal_value(data)