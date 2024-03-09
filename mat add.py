#matrix addition

print("Enter first matrix:")
m=[[0,0,0],[0,0,0],[0,0,0]]
n=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        a=int(input())
        m[i][j]=a
print("Enter second matrix")
for i in range(0,3):
    for j in range(0,3):
        a=int(input())
        n[i][j]=a
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        res[i][j]=m[i][j]+n[i][j]
        print(res[i][j],end=" ")
    print()

#list reverse
t=eval(input("Enter list: "))
l=list(t)
l.sort(reverse=True)
print(l)
