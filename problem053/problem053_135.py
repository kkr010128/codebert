n = int(input())
ns = [int(i) for i in input().split()]
ns.reverse()
if len(ns) > n:
  del ns[:(len(ns) - n)]
for i in ns:
  if i != ns[-1]:
    print(i,end=' ')
  else:
    print(i,end='')
print()