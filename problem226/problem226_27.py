h,n = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
res = "No"
for i in range(n):
  h -= a[i]
  if h <= 0:
    res = "Yes"
print(res)