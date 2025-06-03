a=int(input())
b=list(map(int,input().split()))
b.sort()
c=0
for i in range(a-1):
  if b[i]==b[i+1]:
    c=c+1
if c==0:
  print("YES")
else:
  print("NO")