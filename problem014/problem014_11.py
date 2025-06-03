def bubblesort(A):
    tot = 0
    flag = 1
    N = len(A)
    
    while flag:
        flag = 0
        for j in xrange(N-1,0,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                flag = 1
                tot += 1
    return A,tot

while True:
    try:
        N = int(raw_input())
    except EOFError:
        break
    A = map(int,raw_input().split())
    
    A,tot = bubblesort(A)
    print ' '.join(map(str,A))
    print tot