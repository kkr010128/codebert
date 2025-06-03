from functools import reduce

n = int(input())
a = list(map(int, input().split()))

b = reduce(lambda acc, cur: acc ^ cur, a[1:], a[0])
print(*map(lambda x: x ^ b, a))
