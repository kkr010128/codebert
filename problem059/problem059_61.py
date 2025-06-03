r, c = map(int, input().split())
A = []
for line in range(r):
    A.append(list(map(int, input().split())))

[A[i].append(sum(A[i])) for i in range(r)]

trans = []
for i in range(c+1):
    trans.append([A[j][i] for j in range(r)])
    trans[i].append(sum(trans[i]))

ret = []
for i in range(r+1):
    ret.append([trans[j][i] for j in range(c+1)])
    print(' '.join(map(str, ret[i])))