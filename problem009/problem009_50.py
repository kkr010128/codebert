import collections
n= int(input())
g=[]
for _ in range(n):
    v,k,*varray= map(int,input().split())
    g.append(varray)
        

d= [-1]* (n+10)
d[0]=0
q= collections.deque()
q.append(0)
while len(q)>  0:
    cur = q.popleft()
    for next in g[cur]:
        if d[next-1]== -1:
            d[next-1]= d[cur]+1
            q.append(next-1)
            
for i in range(n):
    print(i+1,d[i])
    
