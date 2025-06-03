N,K = map(int,input().split())
m = 10**9 + 7
ans = 0
cnt_arr = [0]*(K+1)
for i in range(K,0,-1):
  cnt = pow(int(K//i), N, mod=m)
  j = 2
  while i*j<=K:
    cnt -= cnt_arr[i*j]
    j+=1
  cnt_arr[i]=cnt
  ans += i*cnt

print(int(ans%m))