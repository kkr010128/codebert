N = int(input())
A = [int(i) for i in input().split()]
A1 = 1
if 0 in A:
    print(0)
else:    
    for j in range(N):
        A1 *= A[j]
        if A1>10**18:
            print(-1)
            break
    else:
        print(A1)