# Forbidden List

X, N = [int(i) for i in input().split()]
pi = [int(i) for i in input().split()]

pl = []
pu = []
for i in pi:
    if i <= X:
        pl.append(i)
    if X <= X:
        pu.append(i)

pl.sort(reverse=True)
pu.sort()

nl = X
for i in pl:
    if i == nl:
        nl -= 1
nu = X
for i in pu:
    if i == nu:
        nu += 1

if X - nl <= nu - X:
    print(nl)
else:
    print(nu)
