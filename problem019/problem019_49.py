# coding: UTF-8
from collections import deque
queue = deque()
ftime = deque()
n,quantum = map(int,input().split())
for i in range(n):
  name,time = input().split()
  time = int(time)
  queue.append((name,time))

t = 0
while queue:
 name,time = queue.popleft()
 if time <= quantum:
   t += time
   ftime.append(name + " " + str(t))
 else:
   t += quantum
   queue.append((name,time-quantum))

while ftime:
  print(ftime.popleft())
   
 
