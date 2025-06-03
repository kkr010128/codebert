N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(N-K):
    if a[i] < a[i + K]:
        print('Yes')
    else:
        print("No")