N=int(input())
a=list(map(int,input().split()))
s=a[0]
for i in range(1,N):
  s^=a[i]
for i in range(N):
  print(s^a[i])