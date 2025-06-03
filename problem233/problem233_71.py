n=int(input())
p=[int(x) for x in input().split()]
a=1
b=p[0]
for i in range(1,n):
  if p[i-1]<b:
    b=p[i-1]
  if p[i]<=b:
    a+=1
print(a)    