class Student:
     def __init__(self,name,marks):
         self.__name = name
         self.__marks = marks
     def get_name(self):
         return self.__name 
     def get_marks(self):
         return self.__marks
class ResultAnalyzer(Student):
     #def __init__(self,name,marks):
      #  super().__init__(name,marks)
     def get_avgerage(self):
        total = 0
        marks = self.get_marks()
        for i in range(len(marks)):
            total = total+ marks[i]
        average = total/len(marks)
        return total 
     def get_highest(self):
         highest = max(self.get_marks())
         return highest
     def count_passed_subjects(self):
         count = 0
         for i in self.get_marks():
            if i >= 50 :
                count+=1
         return count
     def reverse_name(self):
        return self.get_name()[::-1]
name = input()
name_letters = input()
marks = list(map(int,input().split()))
s1 = ResultAnalyzer(name,marks)
print(f"Name :{s1.get_name()}")
print(f"Reversed Name :{s1.reverse_name()}")
print(f"Average: {s1.get_avgerage()}")
print(f"Highest:{s1.get_highest()}")
print(f"Passed subjects:{s1.count_passed_subjects()}")

'''Important points from the above code is:
--->when we use private variables in the parent class if there is 
no permission to inherit the variables inside the child class we only use the
getter method().
----> if we call any method inside the call we must use self.method_name()
--->
'''
                 
        
              
          