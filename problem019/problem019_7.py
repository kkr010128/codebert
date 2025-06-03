from collections import deque

nameq = deque()
timeq = deque()
n, q = map(int, raw_input().split())
for _ in xrange(n):
  name, time = raw_input().split()
  nameq.append(name)
  timeq.append(int(time))

t = 0
while nameq:
  name = nameq.popleft()
  time = timeq.popleft()
  if time > q:
    time -= q
    nameq.append(name)
    timeq.append(time)
    t += q
  else:
    t += time
    print "%s %d" % (name, t)