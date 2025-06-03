# coding:utf-8
n, k = map(int,raw_input().split())
ws = []
for _ in xrange(n):
  ws.append(int(raw_input()))

def possible_put_p(p):
  # P??\?????????????????????????????????
  current = 1
  weight = 0
  for w in ws:
    if weight + w <= p:
      weight += w
    else:
      current += 1
      if current > k:
        return False
      weight = w

  if current <= k:
    return True
  else:
    return False

low = max(ws)
high = sum(ws)
while(high - low > 0):
  mid = (low + high) / 2
  if(possible_put_p(mid)):
    high = mid
  else:
    low = mid + 1

print high