n=int(input("Enter a number: "))
temp=n
c=0
while(n>0):
    c+=1
    n//=10;
print("Number of digits: ",c)
