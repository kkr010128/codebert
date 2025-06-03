from __future__ import print_function
import time
from sys import stdin
from Queue import Queue
start = time.clock()
i = 0
num=int(stdin.readline())
L=[]
for _ in range(num):
    L.append([int(s) for s in stdin.readline().split()[2:]])
 
d=[-1]*num
d[0]=0
q=Queue(100)
q.put(0)
while not q.empty():
    u=q.get()
    for v in L[u]:
        if d[v-1]<0:
            d[v-1]=d[u]+1
            q.put(v-1)
for i,v in enumerate(d):
    print (i+1,v)