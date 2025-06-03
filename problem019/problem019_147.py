from collections import deque

n,q = map(int,input().split())
Q = deque()

for i in range(n):
    a = input().split()
    Q.append([a[0],int(a[1])])
s = 0

while Q:
    qt = Q.popleft()
    
    if qt[1] > q:
        Q.append([qt[0],qt[1]-q])
        s += q
    else:
        s += qt[1] 
        print(qt[0],s)