from collections import Counter

N,*A = map(int, open(0).read().split())
ac = Counter(A)
if len(ac) == N:
    print('YES')
else:
    print('NO')