def main():
  h,n=map(int,input().split())
  dp=[10**9]*(h+1)
  dp[h]=0
  for i in range(n):
    a,b=map(int,input().split())
    for j in range(h,0,-1):
      nxt=j-a
      if nxt<0:
        nxt=0
      if dp[nxt]>dp[j]+b:
        dp[nxt]=dp[j]+b
  print(dp[0])
main()