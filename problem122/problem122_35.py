n0 = int(1e5)+1
x = [0]*n0

n = int(input())
a0 = list(map(int,input().split()))
q = int(input())
bcs = []
for i in range(q):
    bcs.append(list(map(int,input().split())))

for a in a0:
    x[a] += 1
sum0 = sum(a0)

for bc in bcs:
    sum0 = sum0 + bc[1]*x[bc[0]] - bc[0]*x[bc[0]]
    x[bc[1]] += x[bc[0]]
    x[bc[0]] = 0
    print(sum0)