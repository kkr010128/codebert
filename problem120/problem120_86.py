a, b = map(int, input().split())
c = list(map(int, input().split()))
d = sorted(c)
result = 0
for i in range(b):
    result += d[i]

print(result)
