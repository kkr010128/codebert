def calc(n, x):
    result = 0
    for i in range(3, n + 1):
        for j in range(2, i):
            for k in range(1, j):
                if sum([i, j, k]) == x:
                    result += 1
    return str(result)

ans = []
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    ans.append(calc(n, x))

print("\n".join(ans))
