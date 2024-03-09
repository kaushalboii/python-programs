s1=input("Enter 1st string: ")
s2=input("Enter 2nd string: ")
counter=0
if s1<s2:
    l=len(s1)
else:
    l=len(s2)
for i in range(0,l):
    if s1[i]==s2[i]:
        counter+=1
print(counter)
