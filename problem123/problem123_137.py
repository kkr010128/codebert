n = int(input())
a = list(map(int, input().split()))

b = a[0]
for v in a[1:]:
    b ^= v
print(*map(lambda x: x ^ b, a))
