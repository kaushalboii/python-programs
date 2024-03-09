l=eval(input("Enter the elements of the list: "))
odd,even=0,0
for i in l:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("Sum of even numbers is: ",even,"\nSum of odd numbers is: ",odd)
