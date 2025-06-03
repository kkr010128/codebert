N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

cnt = 0
for i in range(len(A)):
  if i == 0:
    continue
  
  cnt += A[int(i/2)]

print(cnt)
