N = int(input())
A = list(map(int, input().split()))

if N == 0 and A[0] == 1:
  print(1)
  exit(0)
elif A[0] > 0:
  print(-1)
  exit(0)

X = [0] * (N+1)
X[-1] = A[-1]
for i in range(N,0,-1):
  X[i-1] = X[i] + A[i-1]
  
#print(X)

wk = 2
ans = 1
for i in range(1,N+1):
  
  #print(i,X[i])
  if 0 <= A[i] <= wk:
    ans += min(wk,X[i])
    wk -= A[i]
    wk *= 2
  else:
    print(-1)
    exit(0)
  
print(ans)