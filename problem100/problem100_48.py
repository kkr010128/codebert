X = int(input())
rank = -1
if X <= 599:
  rank = 8
elif X <= 799:
  rank = 7
elif X <= 999:
  rank = 6
elif X <= 1199:
  rank = 5
elif X <= 1399:
  rank = 4
elif X <= 1599:
  rank = 3
elif X <= 1799:
  rank = 2
else:
  rank = 1
print(rank)