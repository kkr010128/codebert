from collections import deque

n = int(input())

adj = [0]*n # adjacent list
d = [-1]*n # distance from the source vertex
c = ['w']*n # the 'color' of each vertex

# receiving input (the structure of the graph)
for i in range(n):
    tmp = list(map( int, input().split() ) )
    adj[tmp[0]-1] = list(map(lambda x : x - 1, tmp[2:]))

# set the source vertex
s = 0
d[s] = 0
c[s] = 'g'


Q = deque()
Q.append(s)

while Q:
    u = Q.popleft()
    for v in adj[u]:
        if c[v] == 'w':
            c[v] = 'g'
            d[v] = d[u] + 1
            Q.append(v)
    c[u] = 'b'
    

for i in range(n):
    print(f'{i+1} {d[i]}')


