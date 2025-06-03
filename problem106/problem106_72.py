N = int(input())
ans = [0] * (N + 1)
for x in range(1, 10 ** 2 + 1):
    for y in range(1, 10 ** 2 + 1):
        for z in range(1, 10 ** 2 + 1):
            n = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if N < n:
                continue
            ans[n] += 1
print(*ans[1:], sep='\n')
