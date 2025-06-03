D = int(input())
c = list(map(int, input().split()))
s = []
for i in range(D):
    s.append(list(map(int, input().split())))
t = []
for i in range(D):
    t.append(int(input())-1)
v = 0 
last = [-1 for _ in range(26)]
for d in range(D):
    v += s[d][t[d]]
    last[t[d]]=d
    for i in range(26):
        v -= c[i] * (d - last[i])

    print(v)
