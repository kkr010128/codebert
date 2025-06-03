N, M = map(int, input().split())
SC = [tuple(map(int, input().split())) for _ in range(M)]

for i in range(999):
    si = str(i)
    if len(si) != N:
        continue
    for s, c in SC:
        if si[s-1] != str(c):
            break
    else:
        print(i)
        break
else:
    print(-1)