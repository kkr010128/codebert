N = int(input())
L = list(map(int,input().split()))
cnt = 0
for n in range(N):
  if (n + 1) % 2 == 1 and L[n] % 2 == 1:
    cnt += 1
    
print(cnt)