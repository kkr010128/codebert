from collections import deque
n,q=map(int,raw_input().split())
l=deque([raw_input().split()for _ in range(n)])
t=0
while len(l):
 a,b=l.popleft()
 b=int(b)
 if q<b: t+=q;l.append([a,b-q])
 else:   t+=b;print a,t