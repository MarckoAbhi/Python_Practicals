
# Python program to illustrate __del__
class Student:
       # Initializing
       def __init__(self):
             print('Student table created.')

       # Deleting (Calling destructor)
       def __del__(self):
             print('Destructor called, Student table deleted.')

Stud1 = Student()
del Stud1
