a,b,k = map(int, input().split())
m = k if a > k else a
a -= m
b -= min(k-m, b)
print(f'{a} {b}')