N = int(input())
A = list(map(int, list(input().split())))

total = 0
for i in range(1, N):
  step = A[i-1] - A[i]
  if step > 0 :
    total = total + step
    A[i] = A[i] + step
 
print(total)