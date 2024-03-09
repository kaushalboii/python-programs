#even from 1 to 20
for i in range(0,20,2):
    print(i,end=' ')
#fibonacci
n=int(input("\nEnter n value: "))
a=0;b=1
print(a,b,end=' ')
for i in range(0,n-2):
    temp=a+b
    a=b
    b=temp
    print(temp,end=" ")

#find max among three
a=int(input("\n"))
b=int(input())
c=int(input())
if(a>b and a>c):
    print("Max among three is: ",a)
elif(b>a and b>c):
    print("Max among three is: ",b)
else:
    print("Max among three is: ",c)

#number pattern
r=int(input("Enter n value: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(' 0.',j,end=' ')
    print()
