A, B, K = map(int, input().split())

Taka = max(A-K, 0)
if K <= A:
  Aoki = B
else:
  Aoki = max(0, B-(K-A))

print(Taka, Aoki)