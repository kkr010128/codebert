k, n = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

max_len = 0
for i in range(len(A) - 1):
  if max_len < A[i + 1] - A[i]:
    max_len = A[i + 1] - A[i]

# A[n] -> A[0]
l = (k - A[-1]) + A[0]
if max_len < l:
  max_len = l

print(k - max_len)
