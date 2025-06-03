n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, n - k):
    print("Yes" if a[i + k] > a[i] else "No")