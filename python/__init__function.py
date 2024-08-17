class Person:
 

    # init method or constructor

    def __init__(self, name):

        self.name = "Abhishek"
        
 

    # Sample Method

    def say_hi(self):

        print('Hello, my name is', self.name)
p1 = Person("Abhishek")
p1.say_hi()