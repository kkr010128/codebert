N = int(input())
S = list(map(int,input().split()))
t = 10**18
ans = 1

if 0 in S:
  print(0)
  exit(0)
  
for n in S:
  ans *= n
  if ans > t:
    print(-1)
    exit(0)
  
print(ans)