n, k, s = map(int, input().split())

# 1. 全部10**9
# 2. s=10**9の時, 他は1でok

if s == 10 ** 9:
    a = [5] * n
else:
    a = [10 ** 9] * n
for i in range(k):
    a[i] = s
print(*a)
