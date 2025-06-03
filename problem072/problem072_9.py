N=int(input())
ans = "No"
n=0
for _ in range(N):
    x, y = map(int, input().split())
    if x == y:
        n+=1
    else:
        n = 0
    if n >= 3:
        ans="Yes"
print(ans)
