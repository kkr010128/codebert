n = int(input())
a = list(map(int,input().split()))

ans = 0
tmp = 1
for i in a:
    if i == tmp:
        tmp += 1
    else:
        ans += 1

print(ans if ans != n else -1)
