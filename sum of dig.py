def digsum(a):
    su=0
    while a>0:
        su+=a%10
        a//=10
    return su
n=int(input("Enter a number: "))
s=digsum(n)
while True:
    if s>=10:
        s=digsum(s)
    else:
        break
print(s)
