a, b, m = map(int, input().split())
re = list(map(int, input().split()))
de = list(map(int, input().split()))
mre = min(re)
mde = min(re)
list1 = []
for i in range(m):
  x, y, c = map(int, input().split())
  price = re[x-1] + de[y-1] -c
  list1.append(price)
mlist = min(list1)
m1 = mre + mde

if m1 < mlist:
  print(m1)
else:
  print(mlist)
