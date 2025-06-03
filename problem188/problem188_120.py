x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
import heapq as hp
s = x+y
u = []
hp.heapify(u)
for i in range(a):
    hp.heappush(u,[-p[i],'r'])
for i in range(c):
    hp.heappush(u,[-r[i],'m'])
v = []
hp.heapify(v)
for i in range(b):
    hp.heappush(v,[-q[i],'g'])
for i in range(c):
    hp.heappush(v,[-r[i],'m'])
z = []
ans = 0
hp.heapify(z)
for i in range(a):
    hp.heappush(z,[-p[i],'r'])
for i in range(b):
    hp.heappush(z,[-q[i],'g'])
for i in range(c):
    hp.heappush(z,[-r[i],'m'])
while s and x and y:
    t = hp.heappop(z)
    ans += -t[0]
    if t[1] == 'r':
        x -= 1
        s -=1
    elif t[1] == 'g':
        y -= 1
        s -= 1
    else:
        s -= 1
if s > 0 and x > 0:
    while s:
        t = hp.heappop(z)
        if t[1] == 'g':
            continue
        else:
            ans += -t[0]
            s -= 1
elif s > 0 and y > 0:
    while s:
        t = hp.heappop(z)
        if t[1] == 'r':
            continue
        else:
            ans += -t[0]
            s -= 1
print(ans)