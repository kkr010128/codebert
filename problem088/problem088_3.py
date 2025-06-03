N = int(input())
A = list(map(int, input().split()))


sum_value = 0
for i in range(len(A)-1):
  if A[i] >= A[i+1]:
    x =  A[i] - A[i+1]
    A[i+1] = x + A[i+1]
    sum_value += x

print(sum_value)