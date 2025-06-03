N = int(input())
A = list(map(int, input().split()))
total = 0
for a in A:
  total ^= a
result = []
for a in A:
  result.append(total ^ a)
print(*result)