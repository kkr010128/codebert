a, b, k = map(int, input().split())
takahasi = max(0, a - k)
aoki = max(0, b - max(0, k - a))
print(takahasi, aoki)