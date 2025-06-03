import sys

N = next(sys.stdin.buffer)
X = tuple(map(int, next(sys.stdin.buffer).split()))

min_x = min(X)
max_x = max(X)

stamina = min(sum((p - x) ** 2 for x in X) for p in range(min_x, max_x + 1))

print(stamina)
