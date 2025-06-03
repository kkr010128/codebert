n = int(input())
a = list(map(int, input().split()))
rbg = [0]*3
ans = 1
MOD = 1000000007

for i in a:
  count=0
  flg=True
  for j in range(3):
    if rbg[j]==i:
      count+=1
      if flg:
        rbg[j]+=1
        flg=False
  ans*=count
  ans%=MOD
print(ans)