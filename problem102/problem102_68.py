n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
for i in range(n-k):
  if a[i]<a[i+k]:
    print("Yes")
  else:
    print("No")