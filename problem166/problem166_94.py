s=list(input())
s.reverse()
mod=2019

n=[0]*len(s)
n[0]=1
cnt=[0]*len(s)
cnt[0]=int(s[0])
ans=[0]*2019
answer=0

for i in range(1,len(s)):
  n[i]+=(n[i-1]*10)%mod

for i in range(1,len(s)):
  cnt[i]=(cnt[i-1]+int(s[i])*n[i])%mod

for i in cnt:
  ans[i]+=1

for i in range(len(ans)):
  answer+=(ans[i]*(ans[i]-1))//2

answer+=ans[0]

print(answer)