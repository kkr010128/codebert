n = int(input())
g = []
for i in range(n):
    a = list(map(int,input().split()))
    g.append(a[2:])
d = [0]*n
f = [0]*n
global t
t = 0

def find(x):
    global t
    if len(g[x-1]) == 0:
        t += 1
        f[x-1] = t
    else:
        for i in g[x-1]:
            if d[i-1] == 0:
                t += 1
                d[i-1] = t
                find(i)
        t += 1
        f[x-1] = t

for i in range(n):
    if d[i] == 0:
        t += 1
        d[i] = t
        find(i+1)
for i in range(n):
    print(i+1, d[i], f[i])

