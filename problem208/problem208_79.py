n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

for i in range(10 ** (n - 1) - (n == 1), 10 ** n):
    is_ok = True
    for s, c in sc:
        s -= 1
        if int(str(i)[s]) != c:
            is_ok = False
    if is_ok:
        print(i)
        exit()
print(-1)