n = int(input())
A = list(map(int, input().split()))

now = 1
cnt = 0
for a in A:
    if a == now:
        now += 1
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(n-cnt)