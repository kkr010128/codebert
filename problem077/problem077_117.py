a=list(map(int,input().split()))
c=-10**100
for i in range(2):
  for j in range(2,4):
    b=a[i]*a[j]
    if b>c:
      c=b
print(c)