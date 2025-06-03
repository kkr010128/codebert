#158_D
s = input()
q = int(input())

from collections import deque

s = deque(s)

rev = 1
for _ in range(q):
    Q = list(input().split())
    if Q[0] == "1":
        rev *= -1
    elif Q[0] == "2":
        if (Q[1]=="1" and rev==1) or (Q[1]=="2" and rev==-1):
            s.appendleft(Q[2])
        elif (Q[1]=="2" and rev==1) or (Q[1]=="1" and rev==-1):
            s.append(Q[2])
            
s = "".join(s)
            
if rev == -1:
    s = s[::-1]

print(s)