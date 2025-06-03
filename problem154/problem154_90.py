N, K = map(int, input().split())
A = [-1] * (N+1)
for i in range(K):
  d_list = int(input())
  B = input().split()
  B = [int(x) for x in B]
  for i in range(1, N+1):
    if i in B:
      A[i] = 1
count = 0
for i in range(1, N+1):
  if A[i] == -1:
    count += 1
print(count)