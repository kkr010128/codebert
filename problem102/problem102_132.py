N,K = list(map(int, input().split()))
A = [int(i) for i in input().split()]

for i in range(K,N):
    if A[i] > A[i-K]:
        print("Yes")
    else:
        print("No")