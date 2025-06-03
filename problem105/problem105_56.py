N = int(input())
A = list(map(int,input().split()))
count = 0
for i in range(0,N,2):
  if A[i]%2 != 0:
    count += 1
print(count)