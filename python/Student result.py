# Student result
M1 = int(input("Enter Mark subject 1: "))
M2 = int(input("Enter Mark subject 2: "))
M3 = int(input("Enter Mark subject 3: "))
M4 = int(input("Enter Mark subject 4: "))
M5 = int(input("Enter Mark subject 5: "))
M6 = int(input("Enter Mark subject 6: "))
M7 = int(input("Enter Mark subject 7: "))

Total = M1 + M2 + M3 + M4 + M5 + M6 + M7
per = Total / 7
print(per)
if (per >=60):
	print("First divison")
elif (per >=50 and per <=59):
	print("Second divison")
elif (per >=40 and per<=49):
	print("Third divison")
else:
	print("Fail..")