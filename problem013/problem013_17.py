n = int(raw_input())
maxprofit = -2 * 10 ** 9
minval = int(raw_input())
for _ in xrange(n-1):
  R = int(raw_input())
  maxprofit = max(maxprofit, R-minval)
  minval = min(minval, R)
print maxprofit