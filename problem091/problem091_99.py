n=int(input())

a=input().split(' ')
b=[int(i) for i in a]
s=0
for k in range(2,n):
  for j in range(1,k):
    for i in range(j):
      if (b[i]!=b[j] and b[j]!=b[k] and b[k]!=b[i]):
        m=max(b[i],b[j],b[k])
        if 2*m<b[i]+b[j]+b[k]:
          s+=1
print(s)