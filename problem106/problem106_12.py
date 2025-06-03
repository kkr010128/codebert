n=int(input())
l=[0]*n
q=int(n**0.5)
for i in range(1,q+1):
  for j in range(1,q+1):
    for k in range(1,q+1):
      t=((i+j)**2+(j+k)**2+(i+k)**2)//2
      if t<=n:
        l[t-1]+=1
print(*l)