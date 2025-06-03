import collections

N = int(input())
A = list(map(int, input().split()))

cs = collections.Counter(A)
mcs = cs.most_common()
cnt = mcs[0][1]
if cnt == 1:
    print('YES')
else:
    print('NO')