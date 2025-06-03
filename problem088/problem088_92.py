N = input()
A = list(map(int,input().split()))
raw =sum(A)
con = 0

if len(A) == 1:
    print(0)
    
else:
    for i in A:
        if A[con] > A[con+1]:
            A[con+1] =  A[con]
        
        if A[con+1] == A[-1]:
            break

        con += 1

    ans = sum(A) - raw
    print(ans)