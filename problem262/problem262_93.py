N = int(input())
xyss = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        xyss[i].append((x-1, y))

ans = 0
for ptn in range(1<<N):
    conflict = False
    for i in range(N):
        if (ptn>>i) & 1:
            for x, y in xyss[i]:
                if (ptn>>x) & 1 != y:
                    conflict = True
                    break
        if conflict:
            break
    else:
        num1 = bin(ptn).count('1')
        if num1 > ans:
            ans = num1

print(ans)
