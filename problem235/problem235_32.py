from collections import defaultdict
facts = defaultdict(int)
mod=10**9+7
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
n=int(input())
a=[int(i) for i in input().split()]
for i in range(n):
  for b,p in factorization(a[i]):
    if facts[b]<p:
      facts[b]=p
ans=0
f=1
for k,v in facts.items():
  f*=pow(k,v,mod)
  f%=mod
for i in range(n):
  ans+=f*pow(a[i],mod-2,mod)
  ans%=mod
print(ans)