import itertools
n = int(input())
a = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

able = [0] * (max(n * max(a) + 1, 2001))
for item in itertools.product([0, 1], repeat=n):
    total = sum([i * j for i, j in zip(a, item)])
    able[total] = 1

for m in M:
    print('yes' if able[m] else 'no')

