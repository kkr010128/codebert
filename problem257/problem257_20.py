n = int(input())
arr = list(map(int, input().split()))

cnt = 1
for x in arr:
    if cnt == x:
        cnt = cnt + 1
if cnt == 1:
    print(-1)
else:
    print(n-cnt+1)