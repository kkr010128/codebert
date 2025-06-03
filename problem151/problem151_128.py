#E問題
N, M, K = map(int, input().split())
MOD = 998244353

P = MOD
Y = max(N, M)
inv_t = [0]+[1]
for i in range(2, Y):
  inv_t += [inv_t[P % i] * (P - int(P / i)) % P]
#print(inv_t)
          
if K == N - 1:
  ans = 1
  for i in range(N):
    ans = ans * M % MOD
  print(ans % MOD)
  quit()
  
#if M == 1:
  #if 
  #print("1")
 # quit()
  
# M * ((M - 1) ** (N - L - 1)) * combination(N-1, L)のLを0からKまで足した総和が答え
B = [1] * N
ans1 = 1
for i in range(1, N):
  ans1 = (ans1 * (M - 1)) % MOD
  B[i] = (ans1 * M) % MOD
  
ans = 0
ans2 = 1
#X = 1
for i in range(K + 1):
  if i == 0:
    X = 1
  else:
    X = (X * (N - i) * inv_t[i]) % MOD
  ans2 = X * B[N - 1 - i] % MOD 
  ans += ans2
  ans = ans % MOD
      
print(ans)

