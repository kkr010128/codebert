n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort(reverse = True)
s = sum(a)
res = "Yes"
for i in range(m):
  if a[i] * 4 * m < s:
    res = "No"
print(res)