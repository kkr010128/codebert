from collections import deque

s = input()
Q = int(input())

l = deque()
l.append(s)

rev = True
for i in range(Q):
    q = list(input().split())
    if q[0] == "1":
        rev = not rev
    else:
        if rev:
            if q[1] == "1":
                l.appendleft(q[2])
            else:
                l.append(q[2])
        else:
            if q[1] == "1":
                l.append(q[2])
            else:
                l.appendleft(q[2])

ans = ""    
for i in l:
    ans += i

if not rev:
    print(ans[::-1])
else:
    print(ans)