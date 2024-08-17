try: 
 a = 55 / 0
 print(a)
except:
	print("oops! wrong value")
	
	
	# Python program to convert decimal into other number systems
dec = 31

print("The decimal value of", dec, "is:")

print("the given number","in binary.",bin(dec))

print("the given number","in octal.",oct(dec))

print("the given number","in hexadec.",hex(dec))
