print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1 = int(input("enter value 1: "))
num2 = int(input("enter valuec2: "))
opr = input("enter the opr..(+, -, *, /)")
if opr == "+":
	print(num1 + num2)
elif opr == "-":
	print(num1 - num2)
elif opr == "*":
	print(num1 * num2)
elif opr == "/":
	print(num1 /num2)
else:
	print("invalid opr..")