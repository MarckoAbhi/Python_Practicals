x = input("Enter the name of student =>  ")
z=input("Enter your subject stream=> ")
if z=="Science":    
    a=int(input("Enter the mark of General Hindi => "))
    b=int(input("Enter the mark of English =>  "))
    c=int(input("Enter the mark of Math or Biology=> "))
    d=int(input("Enter the mark of Physics =>  "))
    e=int(input("Enter the mark of Chemistry =>  "))
    print(x,": Your Total Marks out of 500 are: ", a+b+c+d+e)
    y=(( a+b+c+d+e)/500)*100
    print("Your percentage is:",y)

    if  y>=90 :
        print("Grade A")
        print("Excellent")
    elif  75<=y<90 :
        print("Grade B")
        print("Very Good")

    elif  60<=y<75 :
        print("Grade c")
        print("Good")

    else :
        print ("grade d")
        print("Not fare")
        
elif z=="Art":
    f=int(input("Enter the mark of Hindi => "))
    g=int(input("Enter the mark of English or History =>  "))
    h=int(input("Enter the mark of Geography=> "))
    i=int(input("Enter the mark of Economics or Civics=>  "))
    j=int(input("Enter the mark of Sociology =>  "))
    print(x,": Your Total Marks out of 500 are: ", f+g+h+i+j)
    k=(( f+g+h+i+j)/500)*100
    print("Your percentage is:",k)

    if  k>=90 :
        print("Grade A")
        print("Excellent")
    elif  75<=k<90 :
        print("Grade B")
        print("Very Good")

    elif  60<=k<75 :
        print("Grade c")
        print("Good")

    else :
        print ("grade d")
        print("Not fare")
    
    
    

    
    