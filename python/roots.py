import math
a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))
c = int(input("Enter the value c :"))
d = b**2 - 4*a*c
if d > 0:
	r1 = (-b+math.sqrt(d)) / (2*a)
	r2 = (-b-math.sqrt(d)) / (2*a)
	print("Roots are real",r1, "and",r2)
elif d ==0:
		r1 = -b / (2*a)
		print("Roots are rael and same", r1)
else:
	print("No real roots are there")