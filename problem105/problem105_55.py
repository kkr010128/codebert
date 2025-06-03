N = int(input())
n = list(map(int,input().split()))

ans = 0
for i in range(N):
  if n[i] % 2 == 1 and (i-1)%2 == 1:
    ans += 1
    
print(ans)
