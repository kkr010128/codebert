from collections import deque
n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())
points = {"r":r,"s":s,"p":p}
d = {"r":"p","s":"r","p":"s"}
que = deque([None]*k)
ans = 0
for ti in t:
    x = que.popleft()
    if d[ti] != x:
        #print(d[ti])
        que.append(d[ti])
        ans+=points[d[ti]]
    else:
        #print(None)
        que.append(None)
    #que.popleft()
    #print(que,ti)
print(ans)