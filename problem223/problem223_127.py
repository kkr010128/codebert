n, k = map(int, input().split())
lst = list(map(int, input().split()))
temp = sum(lst[:k])
m = sum(lst[:k])
for i in range(k, n):
  temp = temp - lst[i - k] + lst[i]
  m = max(m, temp)
print((m + k) / 2)