N = int(input())
A = list(map(int, input().split()))
hight = A[0]
k = 0
for i in range(1, N):
  if hight > A[i]:
    k += (hight - A[i])
  else:
    hight = A[i]
print(k)