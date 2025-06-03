n=int(input())
s=list()
for i in range(n):
  s.append(input())

import collections

c=collections.Counter(s)



l=list()
max_=0
for cc in c.values():
  max_=max(cc, max_)

for ca,cb in c.items():
  if max_==cb:
    l.append(ca)

l.sort()
for ll in l:
  print(ll)
