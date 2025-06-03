N = int(input())
X = list(map(int, input().split()))
a = sum(X)
b = sum([x * x for x in X])
if a / N - a // N < 0.5:
  c = a // N
else:
  c = a // N + 1
print(N * c * c - 2 * a * c + b)