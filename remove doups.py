t=eval(input())
l=list(t)
res=[]
for i in l:
  if i not in res:
    l.append(i)
print(res)
