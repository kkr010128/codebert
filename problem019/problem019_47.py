n,q=map(int,raw_input().split())

lst = []
for idx in xrange(n):
    name, time = raw_input().split()
    lst.append([name, int(time)])

idx = 0
tot = 0
while True:
  lst[idx][1] = lst[idx][1] - q
  if lst[idx][1] <= 0:
    tot += q + lst[idx][1]
    lst[idx][1] = 0
    print "%s %d" % (lst[idx][0], tot)
    lst.pop(idx)
    if len(lst)==0:
        break
  else:
    tot += q
    idx+=1
  if (idx >= len(lst)):
    idx = 0