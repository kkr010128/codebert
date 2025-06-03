
def gen_factorization(N):
    tables=[-1]*(N+1)
    for i in range(2,N+1):
        if tables[i]!=-1:continue
        tmp=i
        while tmp<=N:
            tables[tmp]=i
            tmp+=i
    def fuctorization(n):
        if n==1:return {1:1}
        elif n<0:n=abs(n)
        if n>N:return "error"
        ans={}
        while n!=1:
            tmp=tables[n]
            #debug print
            #print(tmp,n)
            ans.setdefault(tmp,0)
            ans[tmp]+=1
            n//=tmp
        return ans
    return fuctorization

N=int(input())
f=gen_factorization(10**6+10)
A=list(map(int,input().split()))
primes={}
for i in A:
  d=f(i)
  for j in d:
    primes.setdefault(j,0)
    primes[j]+=1
primes[1]=1
ansMax=max(primes.values())

if ansMax==1:
  print('pairwise coprime')
elif ansMax==N:
  print('not coprime')
else:
  print('setwise coprime')