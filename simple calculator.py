a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("\nOperations:\nAddition: +\nSubtraction: -\nMultiplication: *\nDivision: /\n")
ch=input("Enter operation: ")
if ch=="+":
    res=a+b
elif ch=="-":
    res=a-b
elif ch=="*":
    res=a*b
elif ch=="/":
    res=a/b
else:
    print("Invalid input")
print("Result: ",res)
