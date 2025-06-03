n,k=(int(i) for i in input().split())

a=list(map(int, input().split()))
a.sort()
sum=0
for i in range(k):
  sum+=a[i]
print(sum)
