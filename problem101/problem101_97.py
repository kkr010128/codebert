a,b,c= list(map(int,input().split()))
n = int(input())
ans = "No"

for i in range(n):
  if b <= a:
    b = 2*b
  elif c <= b:
    c = 2*c
    
if a<b<c:
  ans = "Yes"

print(ans)