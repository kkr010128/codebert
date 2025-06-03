n = int(input())
p = []
for i in range(n):
    x,y = map(int,input().split())
    p.append([x,y])
q = []
r = []
for i in range(n):
    q.append(p[i][0]+p[i][1])
    r.append(p[i][0]-p[i][1])
q.sort()
r.sort()
ans = max(abs(q[-1]-q[0]),abs(r[-1]-r[0]))
print(ans)