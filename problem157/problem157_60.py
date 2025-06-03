n = int(input())
a = list(map(int, input().split()))

dict_diffs1 = dict()
dict_diffs2 = dict()
for i in range(1, n+1):
  dict_diffs1[i+a[i-1]] = dict_diffs1.get(i+a[i-1], 0) + 1
  dict_diffs2[i-a[i-1]] = dict_diffs2.get(i-a[i-1], 0) + 1
total = 0
for j in range(1, n+1):
  total += dict_diffs1.get(j-a[j-1], 0)
  total += dict_diffs2.get(j+a[j-1], 0)
total = total//2
print(total)