N,K = map(int,input().split())
A = [int(a) for a in input().split()]

n = 0

for i in range(K,N):
    if A[i] > A[n] :
        print("Yes")
    else:
        print("No")
    n+=1
