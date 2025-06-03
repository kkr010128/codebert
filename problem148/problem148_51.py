A, B, C, K = map(int, input().split())
k = K
a = min(A, k)
k -= a
b = min(B, k)
k -= b
c = min(C, k)
print(a-c)