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

def main():
    n=int(input())
    a=list(map(int,input().split()))
    mod=pow(10,9)+7
    lcma={}
    for ai in a:
      f=factorization(ai)
      for fi in f:
        if fi[0] in lcma:
          lcma[fi[0]]=max(lcma[fi[0]],fi[1])
        else:
          lcma[fi[0]]=fi[1]
    l=1
    for k,v in lcma.items():
      l*=pow(k,v,mod)
      l%=mod
    ans=0
    for ai in a:
      ans+=l*pow(ai,mod-2,mod)
      ans%=mod
    print(ans)

main()
