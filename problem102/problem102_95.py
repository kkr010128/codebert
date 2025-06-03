n, k = map(int, input().split())
l = list(map(int, input().split()))
for i in range(1, n - k + 1):
    print("Yes" if l[i - 1] < l[i + k - 1] else "No")