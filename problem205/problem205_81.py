import collections

n,p=map(int,input().split())
s=input()
arr=[int(s[i]) for i in range(len(s))]
if p==2 or p==5:
  ans=0
  for i in range(n):
    if arr[i]%p==0:
      ans+=i+1
  print(ans)
else:
  dic=collections.defaultdict(int)
  match=[]
  pows=[1]
  for _ in range(n):
    pows.append((pows[-1]*10)%p)
  tmp=0
  for i in range(n-1,-1,-1):
    tmp+=arr[i]*pows[n-1-i]
    tmp%=p
    match.append(tmp)
    dic[tmp]+=1
  match=match[::-1]
  ans=0
  rem=0
  rev=pow(10,p-2,p)
  for i in range(n-1,-1,-1):
    ans+=dic[rem]
    rem+=arr[i]*pows[n-1-i]
    rem%=p
    dic[match[i]]-=1
  print(ans)