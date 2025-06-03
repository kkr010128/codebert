n, k, s = map(int, input().split())
a = [s] * k + [1 if n < s else s + 1] * (n - k)
print(*a)