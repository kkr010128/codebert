N,K=map(int,input().split())
A=0
for a in range(100000000000000):
    if N>K:
        kot=N%K
        if abs(K-kot)>kot:
            print(kot)
            break
        else:
            print(abs(K-kot))
            break
    if N%K==0:
        print(0)
        break
    if N<K:
        if abs(N-K)<N:
            print(abs(N-K))
            break
        else:
            print(N)
            break
    tugi=abs(N-K)
    N=tugi
    A=tugi
    tugi=abs(N-K)
    B=tugi
    N=tugi
    tugi=abs(N-K)
    if A==tugi:
        if B<A:
            print(B)
            break
        else:
       	    print(A)
            break