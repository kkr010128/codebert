def find(A,K):
    ANS = []
    for i in range(K,len(A)):
        # check grade[i] > grade[i-1]
        # gr[i] = A[i]*...*A[i-K+1]
        # gr[i-1] = A[i-1]*...*A[i-K]
        # check A[i] > A[i-K]
        if A[i] > A[i-K]:
            ANS += ["Yes"]
        else:
            ANS += ["No"]
    print("\n".join(ANS))

n,k = list(map(int,input().strip().split()))
A = list(map(int,input().strip().split()))
find(A,k)