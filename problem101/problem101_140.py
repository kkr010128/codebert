import itertools
A,B,C = list(map(int, input().split()))
K = int(input())
ans = False
for p in itertools.product(['a','b','c'], repeat=K):
    A0,B0,C0 = A,B,C
    for e in p:
        if e == 'a':
            A0 = 2*A0
        elif e == 'b':
            B0 = 2*B0
        else:
            C0 = 2*C0
    if A0 < B0 < C0 :
        ans = True
        break
print('Yes' if ans else 'No')
