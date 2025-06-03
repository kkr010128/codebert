from math import gcd
N=int(input())
A = list(map(int,input().split()))

val = A[0]
for i in range(1,N):
    val = gcd(val,A[i])

if val > 1:
    print("not coprime")
    exit()

D = [i for i in range(max(A)+1)]
p = 2

while(p*p<=max(A)):
    if D[p]==p:
        for i in range(2*p,len(D),p):
            if D[i]==i:
                D[i]=p

    p+=1

prime = set()
for a in A:
    tmp=D[a]
    L=set()
    while(a>1):
        a=a//tmp
        L.add(tmp)
        tmp=D[a]
    #print(L)
    for l in L:
        if l in prime:
            #print(D)
            #print(prime)
            print("setwise coprime")
            exit()
        else:
            prime.add(l)
#print(D)
#print(prime)
print("pairwise coprime")