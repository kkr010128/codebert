N = int(input())
a = list(map(int,input().split()))
ans = 0
c = 1
for i in range(N):
    if a[i] == c:
        c += 1
    else:
        ans += 1
if ans == N:  print(-1)
else:  print(ans)