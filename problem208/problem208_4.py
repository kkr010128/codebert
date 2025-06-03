N, M = map(int, input().split())
SC = [tuple(map(int, input().split())) for _ in range(M)]

for num in range(1000):
    if len(str(num)) != N: continue
    for s, c in SC:
        s -= 1
        if str(num)[s] != str(c):
            break
    else:
        print(num)
        exit()
print(-1)