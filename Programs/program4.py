# 4.
# Defines a class "Employee" with an __init__ method to initialize attributes like Name, Designation, and Ph. No. Also, includes a display() method to display employee details using instances.


class Employee:
    def __init__(self, name, designation, phone_number):
        self.name = name
        self.designation = designation
        self.phone_number = phone_number

    def display(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Phone Number: {self.phone_number}")

# Creating an instance of the Employee class
employee = Employee("ABC XYZ", "Software Engineer", "123-456-7890")

# Displaying the details of the employee using the display() method
employee.display()
