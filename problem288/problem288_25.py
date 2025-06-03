def Divisors(n):
    L=[]
    k=1
    while k*k <= n:
        if n%k== 0:
            L.append(k)
        k+=1
    return L

N=int(input())
T=Divisors(N)

M=10**20
for a in T:
    M=min(M,a+(N//a)-2)
print(M)
