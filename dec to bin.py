n=int(input())
s=''
while(n>0):
    temp=n%2
    s+=str(temp)
    n//=2
print(s[::-1])
