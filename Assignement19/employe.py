class Employee:
    employee_count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee_count +=1
    def display_employe(self):
         print(self.name)
         print(self.salary)
    @classmethod
    def  total_employee(cls):
            print(cls.employee_count)
s1 = Employee("kavya",100000)
s1.display_employe()
s2 = Employee("bhagii",10000000)
s2.display_employe()
Employee.total_employee()


     
     
       