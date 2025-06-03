N = int(input())
alist = list(map(int, input().split()))

cnt = 1
ans = 0
for a in alist:
    if a != cnt:
        ans += 1
    else:
        cnt += 1

if ans==N:
    print(-1)
else:
    print(ans)
