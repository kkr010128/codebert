n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k-1, n-1):
    print("Yes" if a[i+1] > a[i-k+1] else "No")