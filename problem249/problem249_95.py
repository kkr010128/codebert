a, b, k = [int(i) for i in input().split()]
a_1 = a
b_1 = b
k_1 = k

if a < k:
  a_1 = 0
  k_1 = k - a
  b_1 = b - k_1
  if b_1 < 0:
    b_1 = 0
else:
  a_1 = a - k
print(a_1, b_1)
