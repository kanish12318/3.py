def divide (a,b):
    if(a<b):
        return 0
    else:
        return 1+divide(a-b,b)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("The result of division is: ",divide(a,b))