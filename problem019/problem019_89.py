# coding: utf-8
# Here your code !
import collections

p,q=map(int,input().split())
count =0

deq = collections.deque()
finished=[]

while 1:
    try:
        deq.append(input().split())
        
    except EOFError:
        break

while deq:
    d = deq.popleft()
    d[1]=int(d[1])
    if d[1]<=q:
        count+=d[1]
        d[1]=count
        finished.append(map(str,d))
    elif d[1]>q:
        d[1]-=q
        count+=q
        deq.append(d)
for f in finished:
    print(" ".join(f))