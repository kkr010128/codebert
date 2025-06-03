N,K = map(int,input().split())
MOD = pow(10,9)+7
ans = 0
for i in range(K,N+2): #KからN+1
  MAX = i*(2*N-i+1)//2
  MIN = i*(i-1)//2
  #print(i,MIN,MAX)
  ans += (MAX-MIN+1)%MOD
print(ans%MOD)