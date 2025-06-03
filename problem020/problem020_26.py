import collections
d=collections.deque()
for _ in range(int(input())):
 e=input()
 if'i'==e[0]:d.appendleft(e.split()[1])
 else:
  if' '==e[6]:
   m=e.split()[1]
   if m in d:d.remove(m)
  elif len(e)%2:d.popleft()
  else:d.pop()
print(*d)
