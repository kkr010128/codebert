#ALDS_3_B 16D8103010K Ko Okasaki

from collections import deque

n,q=map(int,input().split())
que=deque()
for i in range(n):
   name,time=input().split()
   time=int(time)
   que.append([name,time])

t=0

while len(que)>0:
    que_t=que.popleft()
    if que_t[1]>q:
        que_t[1]-=q
        t+=q
        que.append(que_t)
    else:
        t+=que_t[1]
        print(que_t[0],t)
