# # Making heart
# import turtle
# pen = turtle.Turtle()
# def curve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)
# def heart():
#     pen.fillcolor('red')
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     curve()
#     pen.left(120)
#     curve()
#     pen.forward(112)
#     pen.end_fill()
# def text1():
#     pen.up()
#     pen.setpos(-68, 95)
#     pen.down()
#     pen.color("yellow")
#     pen.write("I love you")
# heart()
# text1()
# pen.ht()

email=input("Enter your emailID")

valid_email= False
while not valid_email:
    if "@" in email and "." in email:
        print("Your email ID is valid")
        valid_email =True
    else:
        print("Your email is not valid, try again!!!")
        email = input("please enter your email Id")