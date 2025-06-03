n = int(input())
a = list(map(int, input().split()))
leaf = sum(a) - 1
now = 1
ans = 0
for i, num in enumerate(a):
    ans += now
    now -= num
    if leaf >= now:
        leaf -= now
        now *= 2
    elif leaf > 0:
        now += leaf
        leaf = 0
    if now < 0:
        print(-1)
        exit()
print(ans)
