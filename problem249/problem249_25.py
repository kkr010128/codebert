A,B,K = map(int, open(0).read().split())
if K <= A:
    print(A-K,B)
elif K >= A + B:
    print(0,0)
else:
    print(0,B-K+A)