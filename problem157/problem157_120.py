n = int(input())
a = list(map(int, input().split()))

dict_diffs = dict()
for i in range(1, n+1):
  dict_diffs[i+a[i-1]] = dict_diffs.get(i+a[i-1], 0) + 1
total = 0
for j in range(1, n+1):
  total += dict_diffs.get(j-a[j-1], 0)
print(total)