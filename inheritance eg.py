# the parent class
class employee:
    def __init__(self, Name, emp_id):
        self.name= Name #initialize the name attribute
        self.emp_Id= emp_id # initialize the employee id attribute
    def display_info(self):
        print("Employee Name:",self.name)# printing the name and the employee id
        print("Employee Id:",self.emp_Id)
# sub class 1
class FullTimeEmployee(employee):
    def __init__(self,Name,emp_id,salary):
        super().__init__(Name,emp_id) #i am passing the name and employee id
        self.salary=salary # initalize the salary attribute
# overrided the display info method
    def display_info(self): # this is the method for the child class
        super().display_info() # is the method of the parent class
        print("Employee salary:",self.salary) #printed the remaining attribute_salary
# sub class 2
class partTimeEmployee(employee):
    def __init__(self,Name,emp_Id,hourly_rate,hours_worked):
        super().__init__(Name,emp_Id)
        self.hourly_rate =hourly_rate #initialize hourly rate attribute
        self.hours_worked= hours_worked #initialize the hours worked attribute
# override the display info method
    def display_info(self):
        super ().display_info() # called the parent method[display_info]
        print("Hourly Rate:",self.hourly_rate)# printed the remaining attribute-hour
        print("Hours Worked:",self.hours_worked) #printed the remaining attribute-hour_worked
print("------Full time Employee------")
# employee_1= FullTimeEmployee(employee_1_name,employee_1_Id,employee_1_salary)
employee_1= FullTimeEmployee("melaku",123,10000)
employee_1.display_info()
print("----partTimeEmployee---")
# employee_2= partTimeEmployee(employee_2-name,employee_2_Id,employee_2_hourly_rate,employe_2_hours_worked)
employee_2= partTimeEmployee("Aster",125,120,180)
employee_2.display_info()

    

