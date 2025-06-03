# ABC169 D
N=int(input())

def factorization(N):
    res=[]
    for i in range(2,int(N**(1/2))+2):
        if not N%i:
            r=0
            while not N%i:
                N//=i
                r+=1
            res.append((i,r))
    if N>1:
        res.append((N,1))
    return res

fact=factorization(N)

res=0
for p,r in fact:
    i=1
    while 1:
        if i*(i+1)//2<= r < (i+1)*(i+2)//2:
            break
        else:
            i+=1
    res+=i
print(res)        