matrix=[[1,2,3],[2,3,4],[4,5,6]]
rs=0;cs=0;ds=0
for i in range(0,3):
    for j in range(0,3):
        rs+=matrix[i][j]
        cs+=matrix[j][i]
    ds+=matrix[i][i]
print("Sum of rows: ",rs,"\nSum of columns: ",cs,"\nSum of diagonal elements: ",ds)
