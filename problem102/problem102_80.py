nk=list(map(int, input().split()))
a=list(map(int, input().split()))

n=nk[0]
k=nk[1]

for i in range(n-k):
  if(a[i]<a[i+k]):
    print("Yes")
  else:
    print("No")