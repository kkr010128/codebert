n=int(input())

b=list(map(int,input().split()))

b.sort()
for i in range(n-1):
  if b[i]==b[i+1]:
    print("NO")
    break
  if i==n-2:
    print("YES")