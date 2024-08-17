

# Function to get sum of digits  

def getSum(n): 

    

    sum = 0

    for digit in str(n):  

      sum += int(digit)       

    return sum

   

n =int(input("Please enter the number: "))

print(getSum(n))
