import math
a = int(input("enter the value1:"))
b = int(input("enter the value2:"))
c = int(input("enter the value3:"))
d = b*b - 4*a*c
if d >0:
	r1 = (-b + math.sqrt(d)) /(2*a)
	r2 = (-b - math.sqrt(d)) /(2*a)
	print("roots are real and unequal",r1, "and", r2)
elif d ==0:
	r1 = -b / (2*a)
	print("roots are real and same", r1)
else:
	print("no, real roots are there ")
	