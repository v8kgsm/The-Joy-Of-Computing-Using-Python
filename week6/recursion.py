def fact(n):
    if(n==0):
        return 1
    else:
        return(n*fact(n-1))

n=int(input("Enter a positive number:"))
if(n<0):
    print("Invalid Number.")
else:
    f=fact(n)
    
print("Factorial :",f)
