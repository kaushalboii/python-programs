r=int(input("Readings:"))
price=0
if(r>=100):
    price+=2
    r-=100
if(r>=100):
    price+=3
    r-=100
if(r>=100):
    price+=5
    r-=100
print("EB bill:",price)
