N = int(input())
A = list(map(int,input().split()))
MOD = 1000000007
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

lcma={}
for ai in A:
  f=factorization(ai)
  for fi in f:
    if fi[0] in lcma:
      lcma[fi[0]]=max(lcma[fi[0]],fi[1])
    else:
      lcma[fi[0]]=fi[1]
l=1
for k,v in lcma.items():
  l*=pow(k,v,MOD)
  l%=MOD
ans=0
for ai in A:
  ans+=l*pow(ai,MOD-2,MOD)
  ans%=MOD

print(ans)
