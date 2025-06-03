from collections import OrderedDict
n, x, y = map(int, input().split())
x = x-1
y = y-1
dist_hist = OrderedDict({i: 0 for i in range(1, n)})
for i in range(n-1):
  for j in range(i+1, n):
    if i<=x and j>=y:
      dist = j-i + 1 - (y-x)
    elif i<=x and x<j<y:
      dist = min(j-i, x-i + 1 + y-j)
    elif x<i<y and y<=j:
      dist = min(i-x + 1 + j-y, j-i)
    elif x<i<y and x<j<y:
      dist = min(j-i, i-x + 1 + y-j)
    else:
      dist = j - i
    dist_hist[dist] += 1
[print(value) for value in dist_hist.values()]