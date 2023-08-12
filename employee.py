"""
Q:
Write a Python class Employee with attributes like emp_id, emp_name,
emp_salary, and emp_department and methods like calculate_emp_salary,
emp_assign_department, and print_employee_ details.
Sample Employee Data:
"ADAMS"
'E7876*, 50000, "ACCOUNTING"
"JONES"
"E7499»
45000,
"RESEARCH»
"MARTIN"
"E7900", 50000,
50000, "SALES"
"SMITH", "E7698"*, 55000, "OPERATIONS"
b Use "assign_department' method to change the department of an employee.
a Use "print_employee_details' method to print the details of an employee.
5 Use 'calculate emp salary'
method takes two arguments: salary ark; hours_worked, which is
the number of hours worked by the employee. If the number of hours worked is more than
50, the method computes overtime and adds it to the salary. Overtime is calculated as
following formula:
overtime = hours worked - 50
Overtime amount = (overtime * (salary / 50))

"""
class employee:
    def __init__ (self,emp_name,emp_id,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def get_name(self):
        return self.emp_name
    def get_id(self):
        return self.emp_id
    def get_salary(self):
        return self.emp_salary
    def get_department(self):
        return self.emp_department
    def set_name(self,NewName):
        self.emp_name=NewName
    def set_id(self,NewId):
        self.emp_id=NewId
    def set_salary(self, NewSalary):
        self.emp_salary= NewSalary
    def set_department(self,NewDepartment):
        self.emp_department=NewDepartment
    def print_employee_details(self):   
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    def calculate_emp_salary(self,hours_work):
        if(hours_work>50):
            overtime=hours_work - 50
            overtime_amount=(overtime*(self.emp_salary/50))
            total_salary=overtime_amount+self.emp_salary
        else:
            total_salary = self.emp_salary
        return total_salary
    
    
data = [
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS")
]

#call emp.print_employee_details() method
employees = []
for d in data:
    emp = employee(*d)
    employees.append(emp)
for emp in employees:
    emp.print_employee_details()


#call calculate_emp_salary() method
for emp in employees:
    hours_work = int(input(f"Enter hours worked for  {emp.emp_name}: "))
    total_salary=emp.calculate_emp_salary(hours_work)
    print(f"total salary for {emp.emp_name}:{total_salary}")
    
#call emp_assign_department() method
department=input("Enter a new department: ")
change_department = input("Enter employee name to change department: ")
for emp in employees:
    if emp.emp_name == change_department:
        emp.emp_assign_department(department)
        print(f"{emp.emp_name}'s department has been changed to {department}")
        break    


   
        
       
