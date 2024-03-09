n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
t=n1 & n2
print("Bitwise AND: ",bin(t))
t=n1 | n2
print("Bitwise OR: ",bin(t))
t=n1 ^ n2
print("Bitwise XOR: ",bin(t))
t= n1 << n2
print("Left shift: ",bin(t))
t=n1 >> n2
print("Right shift: ",bin(t))
