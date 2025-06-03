from collections import deque
n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

q = deque([])
points = 0
for i in range(n):
    if i <= k-1:
        if t[i] == 'r':
            points += p
            q.append('p')
        elif t[i] == 's':
            points += r
            q.append('r')
        elif t[i] == 'p':
            points += s
            q.append('s')
    else:
        ban = q.popleft()
        if t[i] == 'r':
            if ban != 'p':
              points += p
              q.append('p')
            else:
                q.append('x')
        elif t[i] == 's':
            if ban != 'r':
              points += r
              q.append('r')
            else:
                q.append('x')
        elif t[i] == 'p':
            if ban != 's':
              points += s
              q.append('s')
            else:
                q.append('x')
                
print(points)