n,m = map(int, input().split())

s = int((n + m) * (n + m -1) / 2)
s -= n * m

print(s)