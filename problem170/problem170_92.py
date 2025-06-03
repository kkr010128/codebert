N,K = list(map(int, input().split()))
mod = int(1e9+7)
# N+1からK個をとる手法
# だけどmin - maxまで一飛ばしで作れるはずなので引き算でもとめてよい
ans = 0
for i in range(K,N+2):
  ans = (ans + i * (N+1-i) + 1) % mod
  
print(ans)