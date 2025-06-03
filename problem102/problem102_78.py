N, K = map(int, input().split())
As = list(map(int, input().split()))

for i in range(K, N):
    if As[i]/As[i-K]>1:
        print("Yes")
    else:
        print("No")
