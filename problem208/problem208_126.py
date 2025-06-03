n,m = map(int, input().split())
s_c = [tuple(map(int, input().split())) for _ in range(m)]

ans = -1

for num in range(1000):
    if len(str(num)) != n: continue

    for s,c in s_c:
        if str(num)[s-1] != str(c):
            break
    else:
        ans = num
        break

print(ans)
