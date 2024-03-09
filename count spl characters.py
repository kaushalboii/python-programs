st=input("Enter a string: ")
spch=0
for i in st:
    if not i.isalnum() and not i.isspace():
        spch+=1
print("Number of special characters is: ",spch)
