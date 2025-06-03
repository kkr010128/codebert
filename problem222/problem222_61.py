N,*A = map(int, open(0).read().split())
if len(set(A)) == len(A):
    print('YES')
else:
    print('NO')