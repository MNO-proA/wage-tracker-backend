import csv
import json
import os
import re

def csv_to_fixture(csv_file_path, model_name, app_name):
    fixture_data = []
    last_emp_number = 0

    def generate_emp_number(last_number):
        new_emp_number = last_number + 1
        return f"JTA{str(new_emp_number).zfill(3)}"

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            fixture_object = {
                "model": f"{app_name}.{model_name.lower()}",
                "fields": {}
            }
            
            # Handle the employee number field
            if 'id' in row and row['id']:
                emp_number = row['id']
                fixture_object["pk"] = emp_number
                # Update last_emp_number if necessary
                numeric_part = re.search(r'\d+$', emp_number)
                if numeric_part:
                    last_emp_number = max(last_emp_number, int(numeric_part.group()))
            else:
                emp_number = generate_emp_number(last_emp_number)
                fixture_object["pk"] = emp_number
                last_emp_number += 1

            for key, value in row.items():
                if key.lower() != 'id':  # Skip the ID field as it's handled separately
                    # Convert empty strings to None (null in JSON)
                    fixture_object["fields"][key.lower()] = None if value == "" else value
            
            fixture_data.append(fixture_object)

    # Generate the output file name in the same directory as the input file
    input_dir = os.path.dirname(csv_file_path)
    base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    output_file = os.path.join(input_dir, f"{base_name}_fixture.json")

    # Write the fixture data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(fixture_data, json_file, indent=2)

    print(f"Fixture file '{output_file}' has been created.")

if __name__ == "__main__":
    csv_to_fixture(r'C:\Users\Ella\Desktop\wage_tracker\employee_records\fixtures\employee1.csv', 'Employee', 'employee_records')
    
    
# python csv_to_fixture.py
# python manage.py loaddata employee1_fixture.json
# cd C:\Users\Ella\Desktop\wage_tracker\employee_records\fixtures