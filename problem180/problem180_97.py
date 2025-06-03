n, k = map(int, input().split())

t = n // k
re = n - t * k


if abs(re - k) < re:
    re = abs(re - k)
    i = True

print(re)
