N = int(input())
XY = []
for _ in range(N):
    A = int(input())
    xy = []
    for _ in range(A):
        x, y = map(int, input().split())
        x -= 1
        xy.append((x, y))
    XY.append(xy)
ans = 0
for s in range(1<<N):
    for i in range(N):
        if s>>i&1:
            for x, y in XY[i]:
                if s>>x&1 != y:
                    break
            else:
                continue
            break
    else:
        ans = max(ans, bin(s).count("1"))
print(ans)
