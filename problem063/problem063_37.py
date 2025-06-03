import sys
s = sys.stdin.read()
s = s.lower()
alp = "qazxswedcvfrtgbnhyujmkiolp"
alp = sorted(alp)
for c in alp:
  print('{} : {}'.format(c,s.count(c)))
