n=int(input("Enter number of rows: "))
num=2
for i in range(0,n+1):
    for j in range(0,i):
        print(num,end=" ")
        num+=2
    print()
