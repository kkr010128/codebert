n,*aa = map(int, open(0).read().split())
from collections import Counter
c = Counter(aa)
for i in range(1,n+1):
  print(c[i])