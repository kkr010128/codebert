def main():
    N = int(input())
    A  = [int(_n) for _n in input().split()]
    if N == 0:
        print(1 if A[0]==1 else -1)
        return

    l = A[-1]
    L = [(1,1)]
    for i in range(1,N):
        L.append((A[i]+1, (L[i-1][1]-A[i-1])*2))
        if (L[i-1][1]-A[i-1])*2 < A[i]:
            print(-1)
            return
    L.append((A[N], (L[N-1][1]-A[N-1])*2))
    # print(L)
    if (L[N-1][1]-A[N-1])*2 < A[N]:
        print(-1)
        return
    
    R = [(A[-1],A[-1])]
    for i in reversed(range(N)):
        R.append(((R[-1][0]+1)//2+A[i], R[-1][1]+A[i]))
    res = 0
    for i in range(N+1):
        r = R[i]
        l = L[N-i]
        if r[0] > l[1] or r[1] < l[0]:
            print(-1)
            return
        # print(r,l)
        res += min(r[1], l[1])
    print(res)

        
main()