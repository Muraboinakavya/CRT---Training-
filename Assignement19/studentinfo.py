class Student:
      def __init__(self):
        self.name = "kavya"
        self.roll_no = 200
        self.marks = 32
      def dispaly_details(self):
         print(self.name)
         print(self.roll_no)
         print(self.marks)
      def is_passed(self):
         if(self.marks>=35):
              print("Passed")
         else:
              print("Failed")
s1 = Student()
s2 = Student()
s1.dispaly_details()
s2.is_passed()