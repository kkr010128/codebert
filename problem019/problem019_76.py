nq = str(input()).split()
n = int(nq[0])
q = int(nq[1])
p = [str(input()).split() for i in range(n)]
p = [(str(i[0]), int(i[1])) for i in p]
ans = []
time = 0
while len(p) != 0:
    t = p.pop(0)
    if t[1] > q:
        #p = [(s[0], s[1], s[2]+q) for s in p]
        time += q
        p.append((t[0], t[1]-q))
    elif t[1] <= q:
        #p = [(s[0], s[1], s[2]+t[1]) for s in p]
        ans.append((t[0], t[1]+time))
        time += t[1]
for t in ans:
    print('{0} {1}'.format(t[0], t[1]))