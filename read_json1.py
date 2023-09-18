import json

# Define the Employee class
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read data from the JSON file
with open("employee.json", "r") as file:
    employee_data = json.load(file)

# Create a list of Employee objects
employee_list = []
for data in employee_data:
    employee = Employee(
        data["Name"],
        data["DOB"],
        data["Height"],
        data["City"],
        data["State"]
    )
    employee_list.append(employee)

# Print the list of Employee objects
for employee in employee_list:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()