n=int(input())
a=list(map(int,input().split()))
c=a[0]
for i in range(1,n):
  c=c^a[i]

for i in range(n):
  print(c^a[i])