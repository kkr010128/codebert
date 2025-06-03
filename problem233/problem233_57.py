N = int(input())
A = list(map(int, input().split()))
min = A[0]
count = 1
for i in range(1, N):
  if A[i] <= min:
    count += 1
    min = A[i]
  else:
    continue
print(count)