print("Matrix before transpose: ")
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in m:
    print(i)
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        res[i][j]=m[j][i]
print("\n\nMatrix after transpose: ")
for i in res:
    print(i)
