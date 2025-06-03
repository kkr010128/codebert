import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A=map(int,read().split())

bound = [0]*(N+1)
bound[0] = 1
#Nが0のとき
if N == 0:
  if A[0] == 1:
    print(1)
  else:
    print(-1)
  sys.exit()
  
#Nが0以外のとき 
#上から
for i in range(1,N+1):
  bound[i] = (bound[i-1]-A[i-1]) *2
  if bound[i] < A[i]:
    print(-1)
    sys.exit()
    
#下からのと最小値を取る
cum_sum = 0 
for i in range(N,-1,-1):
  cum_sum += A[i]
  bound[i] = min(bound[i],cum_sum)
print(sum(bound))
