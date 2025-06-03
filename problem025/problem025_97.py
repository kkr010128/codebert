def main():
    import sys, itertools as ite
    n = int(sys.stdin.readline())
    A = tuple(map(int, sys.stdin.readline().split()))
    #print(A)
    q = int(sys.stdin.readline())
    M = map(int, sys.stdin.readline().split())
    bit = ite.product([0,1], repeat=n)
    ans = []
    for b in bit:
        tmp = 0
        for i in range(n):
            tmp +=b[i]*A[i]
        ans += [tmp]
        
    for m in M:
        if m in ans:
            print('yes')
        else:
            print('no')







if __name__=='__main__':
    main()

