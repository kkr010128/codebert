import itertools

N, M, Q = map(int, input().split())
l = [i for i in range(1, M+1)]
qus = []
As = []
for _ in range(Q):
    b = list(map(int, input().split()))
    qus.append(b)
for v in itertools.combinations_with_replacement(l, N):
    a = list(v)
    A = 0
    for q in qus:
        pre = a[q[1]-1] - a[q[0]-1]
        if pre == q[2]:
            A += q[3]
    As.append(A)
print(max(As))