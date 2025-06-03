n, k = map(int, input().split())
A = list(map(int, input().split()))
now = 1000
for i in range(k, n):
    #print(A[i], A[i-k])
    if A[i] > A[i-k]:
        print("Yes")
    else:
        print("No")