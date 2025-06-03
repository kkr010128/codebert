N=int(input())
a=list(map(int, input().split()))
total=0
for i in range(1,N):
  add=abs(a[i]-a[i-1])
  total=total+add if a[i]<a[i-1] else total
  a[i]=a[i]+add if a[i]<a[i-1] else a[i]

print (total)