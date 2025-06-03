n = int(input())
cnt = 0
mx = -1
ps = []
for _ in range(n):
    d1,d2 = map(int, input().split())
    ps.append((d1,d2))
ps.append((1,2))
for d1,d2 in ps:
    if d1 != d2:
        mx = max(mx,cnt)
        cnt = 0
    else:
        cnt += 1

print("Yes" if mx>=3 else "No")
