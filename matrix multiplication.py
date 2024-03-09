m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[2,3,4],[3,4,5],[4,5,6]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            res[i][j]+= m1[i][k]*m2[k][j]
for i in res:
    print(i)
