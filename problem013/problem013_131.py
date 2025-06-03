n = int(input())
p = [int(input()) for i in range(n)]

max_diff = -float('inf')
min_n = p[0]

for i in range(1, n):
  max_diff = max(max_diff, p[i] - min_n)
  min_n = min(min_n, p[i])

print(max_diff)