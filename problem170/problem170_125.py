n, k =map(int,input().split())
MOD = 10**9 + 7
ans = 0
for i in range(k,n+2):
  L = (i-1)*i / 2  #初項0,末項l,項数iの等差数列の和
  H = ((n-i)+(n+1))*i //2 #初項a,末項l,項数iの等差数列の和
  ans += H - L + 1
  ans %= MOD
print(int(ans))