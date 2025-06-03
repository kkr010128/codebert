A, B, C, K = map(int, input().split())
ret = 0

for numberOfCards, point in [(A, 1), (B, 0), (C, -1)]:
  if K >= numberOfCards:
    K -= numberOfCards
    ret += numberOfCards * point
  else:
    ret += K * point
    break
    
print(ret)
