N = int(input())
cnt = 0
A = list(map(int,input().split()))
for n in range(N):
  if n % 2 == 0 and A[n] % 2 == 1:
    cnt += 1
print(cnt)