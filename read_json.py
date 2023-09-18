import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

for i in range(5):
    print(f"Enter details for Employee {i + 1}:")
    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    height = float(input("Height (in cm): "))
    city = input("City: ")
    state = input("State: ")
    
    employee_data = {
        "Name": name,
        "DOB": dob,
        "Height": height,
        "City": city,
        "State": state
    }
    
    employee_list.append(employee_data)

with open("employee.json", "w") as file:
    json.dump(employee_list, file, indent=4)

print("Employee data saved to 'employee.json'")

with open("employee.json", "r") as file:
    employee_data = json.load(file)

employee_objects = []
for data in employee_data:
    employee = Employee(
        data["Name"],
        data["DOB"],
        data["Height"],
        data["City"],
        data["State"]
    )
    employee_objects.append(employee)

for employee in employee_objects:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()