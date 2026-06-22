'''-------------------------------------------
import datetime as dt 
print(dt.datetime.now())
------------------------------------------------
module                   
#package:
is a folder containing  multiple modules
school/--->package
student.py 
teacher.py
management.py

#TASK:are of the circle
import math
r = 5
print(math.pi * r *r)
#---------------------------------------------------
*****Random builtin methods:used for random values
#1.randint()--->give the random value in integer 
import random 
print(random.randint(1,1000))
2.choice()--->choice the random item in a particular list(or)tuple in any format
friuts = ["banna","apple","mango"]
print(choice.(friuts))
3.random.randam()---->it gives the random value between 0 to 1.0 
print(random.random())
4.shuffle()-->it shuffles the numbers
cards = [1,2,3,4]
random.shuffle(cards)
print(cards)


#task :print the dice simulator 
import math
print(random.randint(1,6))


#date :
import datetime
print(datetime.date.today)


#custome date
date = datetime.date(2026,6,18)
print(date)


#task :biuld age caluclator
birth_date = 2005
current_year = datetime.date.today().year
print(current_year - birth_date) 



when we want to import the one file inside the another file in the same folder:
we write like this:****** from.import filename


change the name(rename):
 import os
 os.rename("file name")


 listdir():it gives the files and folders in your path
 print(os.listdir())


 Remove directory()-->this delete the file you want
 os.rmdir("filename")



 #TASK:to display the all files  in directory
import os
files = os.listdir()
print(files)



#TASK: if you want to choose the system version:
import sys
print(sys.version)
# if you want to exist from the 
print(sys.exit)




import math
print(math._name_)
print(math._doc_)#---->(doc) this gives the methods in that particular function 

'''

import math
import sys
print(sys.path)
print(dir(math))


#pip----->python package manager



#python Virtual environment
  python -m venv env


