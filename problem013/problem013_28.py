n = int(input())
i, j = int(input()), 0
nmin = i
a = -2 * 10 ** 9
for h in range(n - 1):
    j = int(input())
    a = max(a, j - nmin)
    if j < nmin:
        nmin = j

print(a)