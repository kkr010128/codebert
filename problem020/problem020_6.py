from collections import deque
l=deque()
for _ in range(input()):
    a=raw_input().split()
    c=a[0][-4]
    if c=="i":   l.popleft()
    elif c=="L": l.pop()
    elif c=="s": l.appendleft(a[1])
    else:
        try:     l.remove(a[1])
        except:  pass

print " ".join(l)