from collections import deque

n=int(input())
que_r=deque()

for i in range(n):
    s=input()
    l=len(s)
    if s[0]=="i":
        que_r.appendleft(s[7:])
    elif s[6]==" ":
        try:
            que_r.remove(s[7:])
        except: pass
    elif l>10:
        que_r.popleft()
    elif l>6:
        que_r.pop()

print(*que_r)
