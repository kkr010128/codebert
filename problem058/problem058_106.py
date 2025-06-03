list = []
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break

    cnt = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a + b + c == x:
                    cnt += 1
    list.append(cnt)

for s in list:
    print(s)