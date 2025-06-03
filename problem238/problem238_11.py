n, k, s = map(int, input().split())
L = [0] * n
for i in range(n):
    if i < k:
        L[i] = s
    else:
        if s != 10 ** 9:
            L[i] = s + 1
        else:
            L[i] = s - 1
print(*L)
