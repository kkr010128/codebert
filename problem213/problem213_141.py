n = int(input())
lst = [int(i) for i in input().split()]

min_n = min(lst)
max_n = max(lst)
min_count = 1000000000
for i in range(min_n, max_n + 1):
  count = 0
  for j in range(n):
    count += (lst[j] - i) ** 2
  if count < min_count:
    min_count = count
print(min_count)
